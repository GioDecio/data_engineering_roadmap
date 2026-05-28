# Write a SQL query to find the number of stores that each product has been sold in?
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StructField, StructType, IntegerType, StringType
from pyspark_playground.core.utils import show

if __name__ == "__main__":

    spark = SparkSession.builder.appName("ex_custom_1").getOrCreate()

    departments_data = [
        (1, "Food & Drink"),
        (2, "Clothing"),
        (3, "Electronics"),
        (4, "Home & Garden"),
        (5, "Beauty"),
    ]

    department_schema = StructType(
        [
            StructField("department_id", IntegerType(), False),
            StructField("department_name", StringType(), True),
        ]
    )

    df_department = spark.createDataFrame(departments_data, department_schema)

    show(df_department)
