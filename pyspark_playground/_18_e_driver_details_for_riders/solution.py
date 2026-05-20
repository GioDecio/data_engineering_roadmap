# You are given two datasets:

# rides – containing ride-level data such as pickup time, fare amount, and distance.
# drivers – containing driver information including name, status, and rating.
# Your task is to:

# Join both datasets using the driver_id field.
# Select the following columns from the joined data: ride_id, driver_id, driver_name, fare_amount, status.


from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType,
    StringType,
    DoubleType,
)
from pyspark_playground.core.utils import show

spark = SparkSession.builder.getOrCreate()


def driver_details_for_riders(rides_df, drivers_df):

    return rides_df.join(drivers_df, on="driver_id", how="left")


if __name__ == "__main__":
    rides_data = [
        (1, 101, 201, 300.0, 12.4),
        (2, 102, 202, 150.0, 8.0),
        (3, 101, 203, 220.0, 10.5),
        (4, 103, 204, 500.0, 15.6),
        (5, 104, 205, 100.0, 5.0),
        (6, 102, 206, 180.0, 9.2),
        (7, 101, 207, 275.0, 11.8),
        (8, 103, 208, 330.0, 13.0),
        (9, 105, 209, 400.0, 14.0),
        (10, 106, 210, 210.0, 9.0),
    ]

    drivers_data = [
        (101, "Alex", "available", 4.8),
        (102, "Sam", "off_duty", 4.6),
        (103, "Rita", "available", 4.9),
        (104, "John", "suspended", 3.2),
        (105, "Priya", "available", 4.5),
        (106, "Ramesh", "off_duty", 4.3),
    ]

    rides_schema = StructType(
        [
            StructField("ride_id", IntegerType(), True),
            StructField("driver_id", IntegerType(), True),
            StructField("rider_id", IntegerType(), True),
            StructField("fare_amount", DoubleType(), True),
            StructField("distance_km", DoubleType(), True),
        ]
    )

    drivers_schema = StructType(
        [
            StructField("driver_id", IntegerType(), True),
            StructField("name", StringType(), True),
            StructField("status", StringType(), True),
            StructField("rating", DoubleType(), True),
        ]
    )

    rides_df = spark.createDataFrame(rides_data, schema=rides_schema)
    drivers_df = spark.createDataFrame(
        drivers_data, schema=drivers_schema
    ).withColumnRenamed("name", "driver_name")

    show(driver_details_for_riders(rides_df, drivers_df))
