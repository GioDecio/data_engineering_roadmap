from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import Window as W

spark = SparkSession.builder.appName("Spark Playground").getOrCreate()

# Assume the dataframes employee, payroll are already initialized.

# Write the logic and display the final dataframe
employees = employees.select("employee_id", "name", "position")
payroll = payroll.select("employee_id", "hours_worked", "hourly_rate")

df_result = employees.join(payroll, on="employee_id", how="left")
TH = 40.0
sub_condition = (
    TH * F.col("hourly_rate")
    + (F.col("hours_worked") - TH) * F.col("hourly_rate") * 1.5
)
condition = F.when(
    F.col("hours_worked") <= TH, F.col("hours_worked") * F.col("hourly_rate")
).otherwise(sub_condition)

df_result = df_result.withColumn("pay", condition).select(
    "employee_id", "name", "pay", "position"
)
display(df_result)
