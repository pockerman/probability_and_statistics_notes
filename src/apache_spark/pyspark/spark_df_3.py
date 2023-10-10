from pyspark.sql import SparkSession
from pyspark.sql import Row
import sys


APP_NAME = "LOAD_CSV_FILE_TO_SPARK"

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Usage: filename <file>", file=sys.stderr)

    # get a spark session
    spark = SparkSession.builder.appName(APP_NAME).getOrCreate()

    # read the filename from the commandline
    rows = [Row("Alex", "Western Road", "Germany", 2),
            Row("Stewart", "New Road", "France", 64),
            Row("Elina", "Hemmel Area", "Spain", 146)]

    # create the DataFrame
    df = spark.createDataFrame(rows, ["Name", "Street Name", "Country", "Number"])
    df.show()

    spark.stop()



