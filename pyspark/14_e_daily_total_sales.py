from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, col

spark = SparkSession.builder.getOrCreate()

data = [
    (1, 101, "2025-05-10", 2, 25.00),
    (1, 102, "2025-05-10", 1, 15.00),
    (1, 103, "2025-05-11", 3, 30.00),
    (2, 101, "2025-05-10", 2, 40.00),
]

columns = ["store_id", "product_id", "sale_date", "quantity_sold", "total_sales"]

df = spark.createDataFrame(data, columns)

df_result = df.groupBy("store_id", "sale_date").agg({"total_sales": "sum"})

df_result.show()
