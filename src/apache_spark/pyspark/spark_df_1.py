"""Loads a CSV file into Spark
"""

"""Convert a csv file to parquet format.
This application is meant to be submitted on
Spark for execution

"""
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType #programatically specify the schema
from pathlib import Path
import sys
import numpy as np

APP_NAME = "LOAD_CSV_FILE_TO_SPARK"

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Usage: filename <file>", file=sys.stderr)

    # get a spark session
    spark = SparkSession.builder.appName(APP_NAME).getOrCreate()

    # read the filename from the commandline

    # where is the file to read
    filename = Path(sys.argv[1])

    print(f"Loading file {filename}")

    # set the schema using DDL
    schema = "`OBJECTID` INT, `TRIPTYPE` INT, "\
             "`PROVIDERNAME` STRING, `FAREAMOUNT` FLOAT,"\
             "`GRATUITYAMOUNT` FLOAT, `SURCHARGEAMOUNT` FLOAT, "\
             "`EXTRAFAREAMOUNT` FLOAT, `TOLLAMOUNT` FLOAT, "\
             "`TOTALAMOUN` FLOAT, `PAYMENTTYPE` STRING,"\
             "`ORIGINCITY` STRING, `ORIGINSTATE` STRING,"\
             "`ORIGINZIP` STRING, `DESTINATIONCITY` STRING,"\
             "`DESTINATIONSTATE` STRING, `DESTINATIONZIP` STRING,"\
             "`MILEAGE` STRING, `DURATION` STRING,"\
             "`ORIGIN_BLOCK_LATITUDE` STRING, `ORIGIN_BLOCK_LONGITUDE` STRING,"\
             "`ORIGIN_BLOCKNAME` STRING, `DESTINATION_BLOCK_LATITUDE` STRING,"\
             "`DESTINATION_BLOCK_LONGITUDE` STRING, `DESTINATION_BLOCKNAME` STRING,"\
             "`AIRPORT` STRING, `ORIGINDATETIME_TR` STRING, `DESTINATIONDATETIME_TR` STRING"

    # read the file into a Spark DataFrame
    # the schema is inferred and it assumes that
    # a header is contained
    csv_df = (spark.read.format("csv")
              .option("header", "true")
              .option("inferSchema", False)
              .option("delimiter", "|")
              .schema(schema)
              .load(str(filename)))


    print(f"Schema used {csv_df.printSchema()}")

    # specify the schema programmatically
    schema = StructType([StructField("OBJECTID", IntegerType(), False),
                         StructField("PROVIDERNAME", StringType(), False),])

    spark.stop()



