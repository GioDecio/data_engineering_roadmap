# Initialize Spark session
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Spark Playground").getOrCreate()

# Copy the starter code or load the file path available in the problem statement
FILEPATH = "/datasets/customers_raw.csv"

df = spark.read.csv(FILEPATH, inferSchema=True, header=True)

conditions = (df["email"].isNotNull()) & df["customer_id"].isNotNull()

df_result = df.filter(conditions)

# Display the final DataFrame using the display() function.
display(df_result)
