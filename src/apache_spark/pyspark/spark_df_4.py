from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql.functions import expr, col
import sys


APP_NAME = "LOAD_CSV_FILE_TO_SPARK"

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Usage: filename <file>", file=sys.stderr)

    # get a spark session
    spark = SparkSession.builder.appName(APP_NAME).getOrCreate()

    # read the filename from the commandline
    rows = [Row(180.0, 85.0, 35, "M"),
            Row(175.5, 75.5, 25, "M"),
            Row(165.3, 55.3, 19, "F")]

    # create the DataFrame
    df = spark.createDataFrame(rows, ["Height", "Weight", "Age", "Sex"])
    df.show()

    # use expr function
    df.select(expr("Height * 5")).show()

    #...or use column
    df.select("Height", col("Height") * 5, "Weight", col("Weight") * 2, "Age", "Sex").show()

    spark.stop()