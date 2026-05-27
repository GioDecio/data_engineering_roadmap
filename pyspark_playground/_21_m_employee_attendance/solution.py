# You are given a dataset containing employee attendance records across various departments in a company. Each row contains:

# Employee ID
# Department Name
# Date
# Status (Present / Absent / Leave)
# Your task is to pivot the data such that for each employee_id, you display the count of each attendance status (Present, Absent, Leave) as separate columns.


from pyspark_playground.core.base import SparkBase
from pyspark_playground.core.runtime import SparkRuntime
from pyspark_playground.core.utils import show
from pyspark.sql.functions import when, col, count


class Ex21(SparkBase):

    def __init__(self, df, *, runtime: SparkRuntime | None = None):
        super().__init__(runtime=runtime)
        self.df = df

    def solutionWithTempView(self):

        self.df.createOrReplaceTempView("tv")

        query = """
            SELECT employee_id
                , COUNT(CASE WHEN status = 'Present' THEN status END) AS Present
                , COUNT(CASE WHEN status = 'Absent' THEN status END) AS Absent
                , COUNT(CASE WHEN status = 'Leave' THEN status END) AS Leave
            FROM tv
            GROUP BY employee_id
            """

        return self.spark.sql(query)

    def solutionWithPySpark(self):
        df_pivot = self.df.groupBy("employee_id").agg(
            count(when(col("status") == "Present", 1)).alias("Present"),
            count(when(col("status") == "Absent", 1)).alias("Absent"),
            count(when(col("status") == "Leave", 1)).alias("Leave"),
        )

        return df_pivot

    def solutionWithPySparkDynamic(self):

        row_distinct_statuses = self.df.select("status").distinct().collect()
        distinct_statuses = [row["status"] for row in row_distinct_statuses]

        df_pivot = (
            self.df.groupBy("employee_id")
            .pivot("status", distinct_statuses)
            .count()
            .fillna(0)
        )

        return df_pivot.orderBy("employee_id")


if __name__ == "__main__":

    data = [
        (1, "HR", "2025-07-01", "Present"),
        (1, "HR", "2025-07-02", "Absent"),
        (1, "HR", "2025-07-03", "Present"),
        (2, "Finance", "2025-07-01", "Leave"),
        (2, "Finance", "2025-07-02", "Present"),
        (3, "IT", "2025-07-01", "Absent"),
        (3, "IT", "2025-07-02", "Absent"),
        (3, "IT", "2025-07-03", "Present"),
        (4, "IT", "2025-07-01", "Leave"),
        (4, "IT", "2025-07-02", "Leave"),
        (4, "IT", "2025-07-03", "Present"),
    ]

    columns = ["employee_id", "department", "date", "status"]

    runtime = SparkRuntime()
    df = runtime.spark.createDataFrame(data, columns)
    ex = Ex21(df, runtime=runtime)
    show(ex.solutionWithTempView())
    show(ex.solutionWithPySpark())
    show(ex.solutionWithPySparkDynamic())
