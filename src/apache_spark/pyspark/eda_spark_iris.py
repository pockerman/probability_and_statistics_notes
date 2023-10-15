from pathlib import Path
from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql import functions as F
from pyspark.sql.functions import expr, col
import sys

DATA_PATH = Path("/home/alex/qi3/qi3_notes/computational_mathematics/src/datasets/iris.data")
APP_NAME = "EDA Iris data"

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

    # we want to rename the column class to class-idx
    new_df = df.withColumnRenamed("class", "class-idx")

    new_df.printSchema()

    # compute basic statistics
    # how many observations per class
    counts = (new_df.select("class-idx")
               .groupBy("class-idx")
               .count()
               .orderBy("count")
               .show()
               )

    # compute mean values
    (new_df.groupBy("class-idx").agg(
        F.mean("sepal-length"),
        F.mean("sepal-width"),
        F.mean("petal-length"),
        F.mean("petal-width"),
    )).show()

    (new_df.groupBy("class-idx").agg(
        F.max("sepal-length"),
        F.max("sepal-width"),
        F.max("petal-length"),
        F.max("petal-width"),
    )).show()

    (new_df.groupBy("class-idx").agg(
        F.min("sepal-length"),
        F.min("sepal-width"),
        F.min("petal-length"),
        F.min("petal-width"),
    )).show()

    # compute variance
    (new_df.groupBy("class-idx").agg(
        F.var_pop("sepal-length"),
        F.var_pop("sepal-width"),
        F.var_pop("petal-length"),
        F.var_pop("petal-width"),
    )).show()

    # select all the columns from sepal-length column that
    # are greater than the mean
    (new_df.select("sepal-length")
     .where(col("sepal-length") > 6.58)
     .show())

    spark.stop()