from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import col
from pyspark_playground.utils import show

spark = SparkSession.builder.appName("Spark Playground").getOrCreate()


def filter_customers(df: DataFrame) -> DataFrame:
    return (
        df.filter(col("purchase_amount") > 100)
        .filter(col("age") >= 30)
        .select("customer_id", "name", "purchase_amount")
    )


if __name__ == "__main__":
    FILEPATH = "pyspark_playground/datasets/customers.csv"
    df = spark.read.csv(path=FILEPATH, inferSchema=True, header=True)

    show(filter_customers(df))
