from pyspark.sql import SparkSession, DataFrame
import pyspark.sql.functions as F
from pyspark.sql import Window as W

spark = SparkSession.builder.getOrCreate()


def top_5_by_day(df: DataFrame) -> DataFrame:
    df = df.groupBy("sale_date", "product_id").agg(
        F.sum(F.col("total_sales")).alias("total_sales")
    )
    w = W.partitionBy("sale_date").orderBy(F.col("total_sales").desc())
    return (
        df.withColumn("rn", F.row_number().over(w))
        .filter(F.expr("rn <= 5"))
        .orderBy("sale_date", F.desc("total_sales"))
    )


if __name__ == "__main__":
    data = [
        (1, 101, "2025-05-10", 2, 25.00),
        (2, 101, "2025-05-10", 1, 15.00),
        (1, 102, "2025-05-10", 5, 50.00),
        (3, 103, "2025-05-10", 3, 30.00),
        (2, 104, "2025-05-10", 4, 45.00),
        (1, 105, "2025-05-10", 2, 60.00),
        (1, 105, "2025-05-10", 1, 15.00),
        (1, 106, "2025-05-10", 2, 10.00),
        (1, 201, "2025-05-11", 1, 20.00),
        (2, 201, "2025-05-11", 2, 40.00),
        (2, 202, "2025-05-11", 2, 40.00),
        (3, 203, "2025-05-11", 3, 35.00),
        (1, 204, "2025-05-11", 1, 25.00),
        (2, 205, "2025-05-11", 2, 30.00),
        (1, 206, "2025-05-11", 4, 50.00),
    ]
    columns = ["store_id", "product_id", "sale_date", "quantity_sold", "total_sales"]
    df = spark.createDataFrame(data, columns)
    top_5_by_day(df).show()
