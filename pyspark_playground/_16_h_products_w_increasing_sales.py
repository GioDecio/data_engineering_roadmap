# You are given two datasets: one with product details and another with annual sales records.
# Your task is to identify the products whose total sales revenue has increased from one year to the next.
# Only include products that have sales records in both years.

import re

from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import expr, col, coalesce, lit, any_value, collect_list
from utils import show

spark = SparkSession.builder.getOrCreate()


def products_with_increasing_sales_with_coalesce(
    df_products: DataFrame, df_sales: DataFrame
) -> DataFrame:
    df_sales_pivot = (
        df_sales.groupBy("product_id").pivot("year", ["2022", "2023"]).max("revenue")
    )

    df_sales_pivot = df_sales_pivot.withColumnsRenamed(
        {"2022": "revenue_2022", "2023": "revenue_2023"}
    )

    df_sales_pivot = df_sales_pivot.withColumn(
        "revenue_2022", coalesce("revenue_2022", lit(0.0))
    )

    df_sales_pivot = df_sales_pivot.withColumn(
        "delta", expr("revenue_2023 - revenue_2022")
    )

    df_result = df_sales_pivot.filter(col("delta") > 0).join(
        df_products, on="product_id", how="left"
    )

    return df_result.select(
        "product_id", "product_name", "revenue_2022", "revenue_2023"
    )


def products_with_increasing_sales_distinct(
    df_products: DataFrame, df_sales: DataFrame
) -> DataFrame:

    # Only include products that have sales records in both years.
    df_sales = df_sales.filter(col("revenue").isNotNull())

    show(df_sales)

    # Provide distinct_years dynamically
    df_distinct_years = df_sales.select("year").distinct().collect()
    distinct_years_list = [row["year"] for row in df_distinct_years]

    print(distinct_years_list)

    df_sales_pivot = (
        df_sales.groupBy("product_id").pivot("year", distinct_years_list).max("revenue")
    )

    _cols = [
        f"revenue_{col}" if re.search("^\d", col) else col
        for col in df_sales_pivot.columns
    ]
    df_sales_pivot = df_sales_pivot.toDF(*_cols)

    df_sales_pivot = df_sales_pivot.withColumn(
        "delta", expr("revenue_2023 - revenue_2022")
    )

    df_result = df_sales_pivot.filter(col("delta") > 0).join(
        df_products, on="product_id", how="left"
    )

    return df_result.select(
        "product_id", "product_name", "revenue_2022", "revenue_2023"
    )


def products_with_increasing_sales_groupby(
    df_products: DataFrame, df_sales: DataFrame
) -> DataFrame:

    # Only include products that have sales records in both years.
    df_sales = df_sales.filter(col("revenue").isNotNull())

    show(df_sales)

    # Provide distinct_years dynamically
    df_distinct_years = (
        df_sales.groupBy("year")
        .agg(any_value("product_id"))
        .select(collect_list("year").alias("years"))
    )

    distinct_years_list = df_distinct_years.select("years").collect()[0]["years"]

    df_sales_pivot = (
        df_sales.groupBy("product_id").pivot("year", distinct_years_list).max("revenue")
    )

    _cols = [
        f"revenue_{col}" if re.search("^\d", col) else col
        for col in df_sales_pivot.columns
    ]
    df_sales_pivot = df_sales_pivot.toDF(*_cols)

    df_sales_pivot = df_sales_pivot.withColumn(
        "delta", expr("revenue_2023 - revenue_2022")
    )

    df_result = df_sales_pivot.filter(col("delta") > 0).join(
        df_products, on="product_id", how="left"
    )

    return df_result.select(
        "product_id", "product_name", "revenue_2022", "revenue_2023"
    )


def products_with_increasing_sales_rdd(
    df_products: DataFrame, df_sales: DataFrame
) -> DataFrame:

    df_sales = df_sales.filter(col("revenue").isNotNull())

    distinct_years_list = (
        df_sales.select("year").distinct().rdd.flatMap(lambda x: x).collect()
    )

    df_sales_pivot = (
        df_sales.groupBy("product_id").pivot("year", distinct_years_list).max("revenue")
    )

    _cols = [
        f"revenue_{c}" if re.search(r"^\d", c) else c for c in df_sales_pivot.columns
    ]
    df_sales_pivot = df_sales_pivot.toDF(*_cols)

    df_sales_pivot = df_sales_pivot.withColumn(
        "delta", expr("revenue_2023 - revenue_2022")
    )

    df_result = df_sales_pivot.filter(col("delta") > 0).join(
        df_products, on="product_id", how="left"
    )

    return df_result.select(
        "product_id", "product_name", "revenue_2022", "revenue_2023"
    )


if __name__ == "__main__":
    products_data = [
        (1, "Wireless Mouse"),
        (2, "Mechanical Keyboard"),
        (3, "USB-C Hub"),
        (4, "Webcam"),
    ]
    df_products = spark.createDataFrame(products_data, ["product_id", "product_name"])

    sales_data = [
        (1, 2022, 1200.00),
        (1, 2023, 1500.00),
        (2, 2022, 2000.00),
        (2, 2023, 1800.00),
        (3, 2022, 800.00),
        (3, 2023, 900.00),
        (4, 2023, 1100.00),
    ]
    df_sales = spark.createDataFrame(sales_data, ["product_id", "year", "revenue"])

    df_result = products_with_increasing_sales_rdd(df_products, df_sales)
    show(df_result)
