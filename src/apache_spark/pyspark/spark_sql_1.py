from pathlib import Path
from pyspark.sql import SparkSession


DATA_PATH = Path("/home/alex/qi3/qi3_notes/computational_mathematics/src/datasets/iris/iris.data")
APP_NAME = "Spark SQL 1"

if __name__ == '__main__':

    # get a spark session
    spark = SparkSession.builder.appName(APP_NAME).getOrCreate()

    schema = ("`sepal-length` FLOAT, `sepal-width` FLOAT, "
              "`petal-length` FLOAT, `petal-width` FLOAT, `class` STRING")

    # load the data
    df = (spark.read.format("csv")
              .option("header", False)
              .option("inferSchema", False)
              .option("delimiter", ",")
              .schema(schema)
              .load(str(DATA_PATH)))

    df.show(n=10)
    df.printSchema()

    # rename the columns
    # we want to rename the column class to class-idx
    new_df = (df.withColumnRenamed("sepal-length", "sepal_length")
              .withColumnRenamed("sepal-width", "sepal_width")
              .withColumnRenamed("petal-length", "petal_length")
              .withColumnRenamed("petal-width", "petal_width"))

    # create a temporary table
    new_df.createOrReplaceTempView("iris_data_tbl")

    # now we can do SQL queries
    query = """SELECT sepal_length, sepal_width, class FROM iris_data_tbl WHERE 
    sepal_length > 2.3 AND sepal_width > 1.3 ORDER BY sepal_width DESC"""
    spark.sql(query).show(n=10)

    # use the CASE construct
    query = """SELECT sepal_length, petal_length, class, CASE WHEN sepal_length < 2.3 THEN 'SMALL' 
    WHEN sepal_length >= 2.3 AND sepal_length < 5.8 THEN 'MEDIUM' 
    WHEN sepal_length >= 5.8 THEN 'LARGE' 
    END AS Sepal_Length_Size FROM iris_data_tbl ORDER BY class DESC"""
    spark.sql(query).show(n=20)
    spark.stop()