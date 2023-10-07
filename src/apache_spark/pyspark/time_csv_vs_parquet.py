import time

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

    # save the CSV as Parquet
    
    parquet_table_name = "/home/alex/qi3/qi3_notes/mlops/data/taxi_2015_01"
    csv_df.write.parquet(parquet_table_name)
    
    start = time.time()
    csv_df.select(F.mean("FAREAMOUNT"), F.variance("FAREAMOUNT")).show()
    end = time.time()
    
    print(f"Time to calculate from CSV format {end-start}")
    
    parquet_df = (spark.read.format("parquet")
                  .load(parquet_table_name))
    
    
    start = time.time()
    parquet_df.select(F.mean("FAREAMOUNT"), F.variance("FAREAMOUNT")).show()
    end = time.time()
    print(f"Time to calculate from Parquet format {end-start}")
    spark.stop()
    