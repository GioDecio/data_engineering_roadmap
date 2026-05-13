from pyspark.sql import SparkSession, DataFrame
from utils import show

spark = SparkSession.builder.getOrCreate()


def daily_total_sales(df: DataFrame) -> DataFrame:
    return df.groupBy("store_id", "sale_date").agg({"total_sales": "sum"})


if __name__ == "__main__":
    data = [
        (1, 101, "2025-05-10", 2, 25.00),
        (1, 102, "2025-05-10", 1, 15.00),
        (1, 103, "2025-05-11", 3, 30.00),
        (2, 101, "2025-05-10", 2, 40.00),
    ]
    columns = ["store_id", "product_id", "sale_date", "quantity_sold", "total_sales"]
    df = spark.createDataFrame(data, columns)
    show(daily_total_sales(df))
