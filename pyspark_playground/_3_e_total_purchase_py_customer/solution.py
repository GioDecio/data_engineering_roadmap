from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import sum as spark_sum
from pyspark_playground.core.utils import show

spark = SparkSession.builder.appName("Spark Playground").getOrCreate()


def total_purchase_by_customer(df: DataFrame) -> DataFrame:
    return (
        df.groupBy("customer_id")
        .agg(spark_sum("purchase_amount").alias("total_purchase"))
        .orderBy("customer_id")
    )


if __name__ == "__main__":
    FILEPATH = "pyspark_playground/datasets/customer_purchases.csv"
    df = spark.read.csv(FILEPATH, inferSchema=True, header=True)
    show(total_purchase_by_customer(df))
