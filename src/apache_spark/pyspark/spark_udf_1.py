from pathlib import Path
from pyspark.sql import SparkSession
from pyspark.sql.types import FloatType
from pyspark.sql import Row
from pyspark.sql import functions as F
from pyspark.sql.functions import expr, col
import sys

#from pyspark.utils.load_iris_dataset import pyspark_load_iris_dataset
import utils.load_iris_dataset

DATA_PATH = Path("/home/alex/qi3/qi3_notes/computational_mathematics/src/datasets/iris/iris.data")
APP_NAME = "EDA Iris data"


def square(x: float) -> float:
    return x*x

if __name__ == '__main__':

    # get a spark session
    spark = SparkSession.builder.appName(APP_NAME).getOrCreate()

    iris_df = utils.load_iris_dataset.pyspark_load_iris_dataset(spark=spark, data_path=DATA_PATH,
                                        with_column_rename=True)

    iris_df.show(n=10)
    iris_df.printSchema()


    # let Spark know about our UDF
    spark.udf.register("square", square, FloatType())

    # create a tmp table to run queries on it
    iris_df.createOrReplaceTempView("iris_data_set")

    query = "SELECT sepal_length, class, square(sepal_length) FROM iris_data_set WHERE sepal_length > 4.8"
    spark.sql(query).show()

    spark.stop()