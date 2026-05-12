# Initialize Spark session
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    IntegerType,
    DoubleType,
)

schema = StructType(
    [
        StructField("customer_id", IntegerType()),
        StructField("name", StringType()),
        StructField("email", IntegerType()),
        StructField("age", IntegerType()),
        StructField("purchase_amount", DoubleType()),
    ]
)

spark = SparkSession.builder.appName("Spark Playground").getOrCreate()


# Copy the starter code or load the file path available in the problem statement
FILEPATH = "datasets/customers.csv"
df = spark.read.csv(path=FILEPATH, inferSchema=True, header=True)

df_pa_gt_hundred = df.filter(col("purchase_amount") > 100)
df_pa_gt_hundred_age_gt_30 = df_pa_gt_hundred.filter(col("age") >= 30)

df_result = df_pa_gt_hundred_age_gt_30.select("customer_id", "name", "purchase_amount")
# Display the final DataFrame using the display() function.

try:
    display(df_result)
except NameError as e:
    print(f"An error occurred: {e}")
    df_result.show()
