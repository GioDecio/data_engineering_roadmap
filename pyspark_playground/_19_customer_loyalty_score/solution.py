# Your task is to calculate loyalty score for each customer:

# Only the rides with payment types "Card" or "Ryd credits" are eligible.

# Calculate a loyalty score per customer using the following logic:

# Each trip earns 10 points
# Each trip with a non-null rating earns 5 additional points
# Return the customers with the highest loyalty scores. In case of ties, order by customer_id.


from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark_playground.core.utils import show

spark = SparkSession.builder.getOrCreate()


def customer_loyalty_score(rides_df, payment_types_df, ratings_df, customers_df):
    rides_payments_df = rides_df.join(payment_types_df, on="payment_type_id")
    rides_payments_df = rides_payments_df.withColumn(
        "payment_type", F.regexp_replace(F.lower(F.col("payment_type")), " ", "")
    )

    customers_rides_payments_df = customers_df.join(
        rides_payments_df, on="customer_id", how="left"
    ).withColumnRenamed("name", "customer_name")

    df = customers_rides_payments_df.join(ratings_df, on="trip_id", how="left")
    df = df.withColumn(
        "points",
        F.when(
            F.regexp_like(
                F.col("payment_type"),
                F.lit("^cas"),
            ),
            0,
        )
        .when(F.col("payment_type").isNull(), 0)
        .otherwise(10),
    )

    df = df.withColumn(
        "points",
        F.when(
            (F.col("rating").isNotNull()) & (F.col("payment_type") != "cash"),
            F.expr("points + 5"),
        ).otherwise(F.col("points")),
    )

    return (
        df.groupBy("customer_id", "customer_name")
        .agg(F.sum("points").alias("loyalty_score"))
        .orderBy(F.col("loyalty_score").desc(), "customer_id")
    )


if __name__ == "__main__":
    # Rides data
    rides_data = [
        (1, 101, 1),
        (2, 102, 2),
        (3, 101, 1),
        (4, 103, 3),
        (5, 104, 1),
        (6, 102, 3),
        (7, 101, 2),
        (8, 105, 3),
        (9, 106, 1),
        (10, 107, 2),
        (11, 108, 1),
        (12, 103, 1),
    ]
    rides_columns = ["trip_id", "customer_id", "payment_type_id"]
    rides_df = spark.createDataFrame(rides_data, rides_columns)

    # Payment types data
    payment_types_data = [
        (1, "Card"),
        (2, "Cash"),
        (3, "Ryd credits"),
    ]
    payment_types_columns = ["payment_type_id", "payment_type"]
    payment_types_df = spark.createDataFrame(payment_types_data, payment_types_columns)

    # Ratings data
    ratings_data = [
        (1, 4.5),
        (3, 3.0),
        (4, 5.0),
        (6, 4.0),
        (8, 4.8),
        (10, 3.7),
        (12, 4.1),
    ]
    ratings_columns = ["trip_id", "rating"]
    ratings_df = spark.createDataFrame(ratings_data, ratings_columns)

    # Customers data
    customers_data = [
        (101, "Alice"),
        (102, "Bob"),
        (103, "Carol"),
        (104, "David"),
        (105, "Eva"),
        (106, "Frank"),
        (107, "Grace"),
        (108, "Helen"),
        (109, "Ivy"),
    ]
    customers_columns = ["customer_id", "name"]
    customers_df = spark.createDataFrame(customers_data, customers_columns)

    show(customer_loyalty_score(rides_df, payment_types_df, ratings_df, customers_df))
