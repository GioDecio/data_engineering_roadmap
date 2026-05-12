from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import regexp_extract, col, expr

spark = SparkSession.builder.appName("PlayerStats").getOrCreate()


def top_players_regex(players_df: DataFrame, countries_df: DataFrame) -> DataFrame:
    players_df = (
        players_df
        .withColumn("playername", regexp_extract(col("player"), r"^([^-]+)", 1))
        .withColumn("SRT", regexp_extract(col("player"), r"-(.+)$", 1))
        .withColumn("50s", regexp_extract(col("50s/100s"), r"^(\d+)", 1))
        .withColumn("100s", regexp_extract(col("50s/100s"), r"/(\d+)$", 1))
        .withColumn("sum", expr("CAST(`50s` AS INT) + CAST(`100s` AS INT)"))
    )
    return (
        players_df.join(countries_df, on="SRT", how="left")
        .select("playername", "country", "runs", "sum")
        .filter(col("sum") > 95)
        .sort(col("runs").desc())
    )


if __name__ == "__main__":
    players_data = [
        ("Sachin-IND", 18694, "93/49"),
        ("Ricky-AUS", 11274, "66/31"),
        ("Lara-WI", 10222, "45/21"),
        ("Rahul-IND", 10355, "95/11"),
        ("Jhonnty-SA", 7051, "43/5"),
        ("Hayden-AUS", 8722, "67/19"),
    ]
    countries_data = [
        ("IND", "India"),
        ("AUS", "Australia"),
        ("WI", "WestIndies"),
        ("SA", "SouthAfrica"),
    ]
    players_df = spark.createDataFrame(players_data, ["player", "runs", "50s/100s"])
    countries_df = spark.createDataFrame(countries_data, ["SRT", "country"])
    top_players_regex(players_df, countries_df).show()
