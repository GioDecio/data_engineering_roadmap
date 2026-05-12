# You are given a dataset containing information about trips, including their cost and customer ratings. Your task is to detect and remove outliers from the trip_cost and rating columns.

# An outlier is any value that falls outside the following range:

# [Q1 - 1.5 × IQR, Q3 + 1.5 × IQR]
# Where:

# Q1 is the 25th percentile (first quartile)
# Q3 is the 75th percentile (third quartile)
# IQR = Q3 - Q1
# Use PySpark's approxQuantile function to compute Q1 and Q3 for each column. Remove rows that are outliers in either trip_cost or rating. Keep the relative error parameter of the function as 0.

from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import col
from functools import reduce

spark = SparkSession.builder.getOrCreate()


def get_quantiles(
    df: DataFrame, prob: list, picked_quantiles: list, header: list, error: float = 0
) -> dict:
    quantiles = df.approxQuantile(header, prob, error)

    picked_quantiles.sort()
    quantiles.sort()
    return dict(zip(picked_quantiles, quantiles))


def remove_outliers_from_trip(df):

    picked_quantiles = ["Q1", "Q3"]
    prob = [0.25, 0.75]

    trip_cost_quantiles = get_quantiles(df, prob, picked_quantiles, "trip_cost")
    rating_quantiles = get_quantiles(df, prob, picked_quantiles, "rating")

    TCQ1 = trip_cost_quantiles["Q1"]
    TCQ3 = trip_cost_quantiles["Q3"]
    TCIQR = TCQ3 - TCQ1

    RQ1 = rating_quantiles["Q1"]
    RQ3 = rating_quantiles["Q3"]
    RIQR = RQ3 - RQ1

    tc_outliers_condition = (col("trip_cost") >= TCQ1 - 1.5 * (TCIQR)) & (
        col("trip_cost") <= TCQ3 + 1.5 * (TCIQR)
    )

    rating_condition = (col("rating") >= RQ1 - 1.5 * (RIQR)) & (
        col("rating") <= RQ3 + 1.5 * (RIQR)
    )

    df = df.filter((tc_outliers_condition) & (rating_condition))

    return df


def iqr_bounds(q1: float, q3: float) -> tuple[float, float]:
    iqr = q3 - q1
    return q1 - 1.5 * iqr, q3 + 1.5 * iqr


def remove_outliers_from_trip_improved(df):

    prob = [0.25, 0.75]
    headers = ["trip_cost", "rating"]

    quantiles = df.approxQuantile(headers, prob, 0)

    tc_q1, tc_q3 = quantiles[0]
    r_q1, r_q3 = quantiles[1]

    tc_outliers_condition = (col("trip_cost") >= tc_q1 - 1.5 * (tc_q3 - tc_q1)) & (
        col("trip_cost") <= tc_q3 + 1.5 * (tc_q3 - tc_q1)
    )

    rating_condition = (col("rating") >= r_q1 - 1.5 * (r_q3 - r_q1)) & (
        col("rating") <= r_q3 + 1.5 * (r_q3 - r_q1)
    )

    df = df.filter((tc_outliers_condition) & (rating_condition))

    return df


def remove_outliers_generic(df: DataFrame, headers: list[str]) -> DataFrame:
    quantiles = df.approxQuantile(headers, [0.25, 0.75], 0)

    conditions = [
        col(c).between(*iqr_bounds(q[0], q[1])) for c, q in zip(headers, quantiles)
    ]

    print(conditions)

    return df.filter(reduce(lambda a, b: a & b, conditions))


data = [
    (1, 250.0, 4.2),
    (2, 270.0, 3.8),
    (3, 1200.0, 4.5),
    (4, 80.0, 2.5),
    (5, 240.0, 1.2),
    (6, 230.0, 4.8),
    (7, 245.0, 4.1),
    (8, 255.0, 4.0),
    (9, 260.0, 5.4),
    (10, 265.0, 3.9),
    (11, 275.0, 4.3),
    (12, 100.0, 0.5),
    (13, 950.0, 4.7),
    (14, 300.0, 4.0),
    (15, 400.0, 1.0),
]

columns = ["trip_id", "trip_cost", "rating"]
df = spark.createDataFrame(data, columns)

df_result = remove_outliers_generic(df, ["trip_cost", "rating"])
df_result.show()
