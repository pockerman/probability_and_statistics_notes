from pyspark.sql import SparkSession


APP_NAME="Hello PySpark"

if __name__ == '__main__':

    # we need a SparkSession object n order
    # to be able to use the Spark API

    spark = SparkSession.builder.appName(APP_NAME).getOrCreate()

    print(f"Running spark app {APP_NAME}")
    spark.stop()