from pyspark.sql import SparkSession, DataFrame
import pyspark.sql.functions as F
from utils import show

spark = SparkSession.builder.appName("Spark Playground").getOrCreate()


def transform_orders(df: DataFrame) -> DataFrame:
    return (
        df.withColumn("products_exploded", F.explode("products"))
        .withColumn("product_name", F.col("products_exploded.product_name"))
        .withColumn("product_price", F.col("products_exploded.product_price"))
        .select("customer_id", "order_id", "product_name", "product_price")
    )


if __name__ == "__main__":
    PATH = "pyspark_playground/datasets/orders.json"
    df = spark.read.json(PATH, multiLine=True)
    show(transform_orders(df))
