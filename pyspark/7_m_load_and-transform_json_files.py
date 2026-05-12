# Initialize Spark session
from pyspark.sql import SparkSession
import pyspark.sql.functions as F

spark = SparkSession.builder.appName("Spark Playground").getOrCreate()

# Copy the starter code or load the file path available in the problem statement
PATH = "/datasets/orders.json"

df = spark.read.json(PATH, multiLine=True)
df = df.withColumn("products_exploded", F.explode("products"))
df = df.withColumn("product_name", df["products_exploded"]["product_name"]).withColumn(
    "product_price", df["products_exploded"]["product_price"]
)
df_result = df.select("customer_id", "order_id", "product_name", "product_price")

# Display the final DataFrame using the display() function.
display(df_result)
