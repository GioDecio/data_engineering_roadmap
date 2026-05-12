from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import split, col, expr

spark = SparkSession.builder.appName("PlayerStats").getOrCreate()


def top_players(players_df: DataFrame, countries_df: DataFrame) -> DataFrame:
    players_df = (
        players_df
        .withColumn("playername", split(col("player"), "-")[0])
        .withColumn("SRT", split(col("player"), "-")[1])
        .withColumn("50s", split(col("50s/100s"), "/")[0].cast("int"))
        .withColumn("100s", split(col("50s/100s"), "/")[1].cast("int"))
        .withColumn("sum", expr("`50s` + `100s`"))
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
    top_players(players_df, countries_df).show()
