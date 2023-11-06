from pathlib import Path
from pyspark.sql import SparkSession

def pyspark_load_iris_dataset(spark: SparkSession, data_path: Path,
                              with_column_rename: bool=True):
    schema = ("`sepal-length` FLOAT, `sepal-width` FLOAT, "
              "`petal-length` FLOAT, `petal-width` FLOAT, `class` STRING")

    # load the data
    df = (spark.read.format("csv")
          .option("header", False)
          .option("inferSchema", False)
          .option("delimiter", ",")
          .schema(schema)
          .load(str(data_path)))

    if with_column_rename:
        new_df = (df.withColumnRenamed("sepal-length", "sepal_length")
         .withColumnRenamed("sepal-width", "sepal_width")
         .withColumnRenamed("petal-length", "petal_length")
         .withColumnRenamed("petal-width", "petal_width"))
        return new_df

    return df