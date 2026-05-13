from pyspark.sql import SparkSession, DataFrame
from pyspark.sql import functions as F
from utils import show

spark = SparkSession.builder.appName("Spark Playground").getOrCreate()


def calculate_payroll(employees: DataFrame, payroll: DataFrame) -> DataFrame:
    df = employees.select("employee_id", "name", "position").join(
        payroll.select("employee_id", "hours_worked", "hourly_rate"),
        on="employee_id",
        how="left",
    )
    TH = 40.0
    pay = F.when(
        F.col("hours_worked") <= TH,
        F.col("hours_worked") * F.col("hourly_rate"),
    ).otherwise(
        TH * F.col("hourly_rate")
        + (F.col("hours_worked") - TH) * F.col("hourly_rate") * 1.5
    )
    return df.withColumn("pay", pay).select("employee_id", "name", "pay", "position")


if __name__ == "__main__":
    employees_data = [
        (1, "Alice", "Engineer"),
        (2, "Bob", "Manager"),
        (3, "Carol", "Analyst"),
    ]
    payroll_data = [
        (1, 38.0, 50.0),
        (2, 45.0, 60.0),
        (3, 40.0, 40.0),
    ]
    employees = spark.createDataFrame(employees_data, ["employee_id", "name", "position"])
    payroll = spark.createDataFrame(payroll_data, ["employee_id", "hours_worked", "hourly_rate"])
    show(calculate_payroll(employees, payroll))
