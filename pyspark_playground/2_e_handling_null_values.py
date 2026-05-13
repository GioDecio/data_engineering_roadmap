from pyspark.sql import SparkSession, DataFrame
from utils import show

spark = SparkSession.builder.appName("Spark Playground").getOrCreate()


def filter_null_values(df: DataFrame) -> DataFrame:
    return df.filter(df["email"].isNotNull() & df["customer_id"].isNotNull())


if __name__ == "__main__":
    FILEPATH = "pyspark_playground/datasets/customers_raw.csv"
    df = spark.read.csv(FILEPATH, inferSchema=True, header=True)
    show(filter_null_values(df))
