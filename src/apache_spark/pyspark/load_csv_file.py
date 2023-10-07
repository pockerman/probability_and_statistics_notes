"""Loads a CSV file into Spark
"""

"""Convert a csv file to parquet format.
This application is meant to be submitted on
Spark for execution

"""
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pathlib import Path
import sys
import numpy as np


APP_NAME="LOAD_CSV_FILE_TO_SPARK"

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Usage: filename <file>", file=sys.stderr)

    # get a spark session
    spark = SparkSession.builder.appName(APP_NAME).getOrCreate()


    # read the filename from the commandline

    # where is the file to read
    filename = Path(sys.argv[1])
    
    print(f"Loading file {filename}")

    # read the file into a Spark DataFrame
    # the schema is inferred and it assumes that
    # a header is contained
    csv_df = (spark.read.format("csv")
              .option("header", "true")
              .option("inferSchema", "true")
              .option("delimiter", "|")
              .load(str(filename)))

    
    
    # how many rows the file has
    n_total_rows = csv_df.count()

    # let see the top 10 rows of the DataFrame
    csv_df.show(n=10, truncate=False)
    
    print(f"Total number of rows {n_total_rows}")
    
    # let's calculate the mean of the FAREAMOUNT column
    total_fareamount_sum = csv_df.select(F.sum("FAREAMOUNT")).collect()[0][0]
    print(f"Total fareamount sum {total_fareamount_sum}")
    print(f"Mean value is  {total_fareamount_sum / n_total_rows}")
    
    # collect the values in a numpy and do statistics.
    # this is not done in parallel
    
    fare_values = csv_df.select("FAREAMOUNT").collect()

    # drop the NULL
    fare_values = [float(row['FAREAMOUNT']) for row in fare_values if row['FAREAMOUNT'] != 'NULL']
    print(f"Mean value {np.mean(fare_values)}")
    print(f"Variance value {np.var(fare_values)}")
    
    csv_df.select(F.mean("FAREAMOUNT"), F.variance("FAREAMOUNT")).show()
    
    
    spark.stop()
    
    
    
