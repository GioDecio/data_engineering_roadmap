from pyspark.sql import SparkSession
from pyspark.sql.functions import split, col, expr

# Initialize Spark session
spark = SparkSession.builder.appName("PlayerStats").getOrCreate()

# Create players_df
players_data = [
    ("Sachin-IND", 18694, "93/49"),
    ("Ricky-AUS", 11274, "66/31"),
    ("Lara-WI", 10222, "45/21"),
    ("Rahul-IND", 10355, "95/11"),
    ("Jhonnty-SA", 7051, "43/5"),
    ("Hayden-AUS", 8722, "67/19"),
]

players_df = spark.createDataFrame(players_data, ["player", "runs", "50s/100s"])

# Create countries_df
countries_data = [
    ("IND", "India"),
    ("AUS", "Australia"),
    ("WI", "WestIndies"),
    ("SA", "SouthAfrica"),
]

countries_df = spark.createDataFrame(countries_data, ["SRT", "country"])

# Your solution starts here
players_df = players_df.withColumn("playername", split(col("player"), "-")[0])
players_df = players_df.withColumn("SRT", split(col("player"), "-")[1])
players_df = players_df.withColumn("50s", split(col("50s/100s"), "/")[0].cast("int"))
players_df = players_df.withColumn("100s", split(col("50s/100s"), "/")[1].cast("int"))
players_df = players_df.withColumn("sum", expr("+".join(["`50s`", "`100s`"])))

df_result = players_df.join(countries_df, on="SRT", how="left")
df_result = (
    df_result.select("playername", "country", "runs", "sum")
    .filter(col("sum") > 95)
    .sort(col("runs").desc())
)

# Display the final DataFrame using the display() function.
df_result.show()
