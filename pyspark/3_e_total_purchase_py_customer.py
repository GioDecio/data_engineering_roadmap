# Initialize Spark session
from pyspark.sql import SparkSession
from pyspark.sql.functions import sum as spark_sum

spark = SparkSession.builder.appName("Spark Playground").getOrCreate()

# Copy the starter code or load the file path available in the problem statement
FILEPATH = "/datasets/customer_purchases.csv"
df = spark.read.csv(FILEPATH, inferSchema=True, header=True)
df_result = (
    df.groupBy("customer_id")
    .agg(spark_sum("purchase_amount").alias("total_purchase"))
    .orderBy("customer_id")
)

# .agg({"purchase_amount":"sum"}).alias("total_purchase") #.order_by("total_purchase")
# df_result = df_result.withColumnRenamed("sum(purchase_amount)", "total_purchase").orderBy("customer_id")

# Display the final DataFrame using the display() function.
display(df_result)
