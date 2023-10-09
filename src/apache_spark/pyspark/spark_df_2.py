"""Loads a CSV file into Spark
"""

"""Convert a csv file to parquet format.
This application is meant to be submitted on
Spark for execution

"""
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType #programatically specify the schema


APP_NAME = "LOAD_CSV_FILE_TO_SPARK"

if __name__ == '__main__':

    # get a spark session
    spark = SparkSession.builder.appName(APP_NAME).getOrCreate()

    # set the schema using DDL
    schema = "`OBJECTID` INT, `TRIPTYPE` INT, `PROVIDERNAME` STRING, `FAREAMOUNT` FLOAT"

    # specify the schema programmatically
    schema = StructType([StructField("OBJECTID", IntegerType(), False),
                         StructField("TRIPTYPE", IntegerType(), False),
                         StructField("PROVIDERNAME", StringType(), False),
                         StructField("FAREAMOUNT", FloatType(), False)])

    data = [[1, 3, "NEW-YORK", 20.0],
            [2, 2, "CAMBRIDGE", 18.2],
            [3, 3, "NEW-YORK", 20.0],
            [4, 2, "LONDON", 25.0],
            [5, 2, "OXFORD", 15.0]]


    df = spark.createDataFrame(data, schema)
    df.show()

    print(f"Schema used {df.printSchema()}")



    spark.stop()



