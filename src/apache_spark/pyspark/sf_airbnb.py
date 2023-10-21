from pathlib import Path
from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.ml import Pipeline

from pyspark.sql import Row
from pyspark.sql import functions as F
from pyspark.sql.functions import expr, col
import sys


DATA_PATH = Path("/home/alex/qi3/qi3_notes/computational_mathematics/src/datasets/sf_airbnb/sf-airbnb-clean.parquet")
APP_NAME = "SF AirBnB"
SEED = 42

if __name__ == '__main__':
    # get a spark session
    spark = SparkSession.builder.appName(APP_NAME).getOrCreate()

    # load data
    airbnb_df = spark.read.parquet(str(DATA_PATH))

    # select the columns
    airbnb_df.select("neighbourhood_cleansed", "room_type", "bedrooms",
                    "bathrooms", "number_of_reviews", "price").show(n=5)

    train_df, test_df = airbnb_df.randomSplit([0.8, 0.2], seed=SEED)

    # print train/test sizes
    print(f"Size of training set: {train_df.count()}")
    print(f"Size of test set: {test_df.count()}")


    vec_assembler = VectorAssembler(inputCols=["bedrooms"], outputCol="features")
    vec_train_df = vec_assembler.transform(train_df)

    vec_train_df.select("bedrooms", "features", "price").show(10)

    lr = LinearRegression(featuresCol="features", labelCol="price")
    lr_model = lr.fit(vec_train_df)

    # investigate the learnt parameters
    m = round(lr_model.coefficients[0],2)
    b = round(lr_model.intercept, 2)
    print(f"Model trained: print={m}*bedrooms + {b}")

    pipeline = Pipeline(stages=[vec_assembler, lr])
    pipeline_model = pipeline.fit(train_df)

    # apply pipeline to test data
    pred_df = pipeline_model.transform(test_df)
    pred_df.select("bedrooms", "features", "price").show(10)