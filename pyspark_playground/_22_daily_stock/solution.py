# You are given a dataset that contains daily closing stock prices for different companies.
# Each row represents the stock symbol, date, and closing price for that day.
# Your task is to calculate the daily price change for each stock by comparing the current day’s price with the previous trading day for the same stock.
# If there is no previous trading day (first date for that stock), the change should be null.

from pyspark_playground.core.base import SparkBase
from pyspark_playground.core.runtime import SparkRuntime
from pyspark.sql.functions import lag, col
from pyspark.sql import Window
from pyspark_playground.core.utils import show


class Ex22(SparkBase):

    def __init__(self, df, *, runtime: SparkRuntime | None = None):
        super().__init__(runtime=runtime)
        self.df = df

    def solutionWithTempView(self):
        self.df.createOrReplaceTempView("daily_stock")

        query = """
        SELECT *
            , closing_price - LAG(closing_price) OVER(PARTITION BY stock_symbol ORDER BY trade_date) AS daily_price_change
        FROM daily_stock
        """

        return self.spark.sql(query)

    def solutionWithPySpark(self):

        w = Window.partitionBy("stock_symbol").orderBy("trade_date")
        self.df = self.df.withColumn(
            "daily_price_change", col("closing_price") - lag("closing_price").over(w)
        )

        return self.df


if __name__ == "__main__":
    data = [
        # AAPL
        ("AAPL", "2023-10-23", 148.0),
        ("AAPL", "2023-10-24", 149.5),
        ("AAPL", "2023-10-25", 150.0),
        ("AAPL", "2023-10-26", 150.0),
        ("AAPL", "2023-10-27", 152.5),
        ("AAPL", "2023-10-30", 151.0),
        # GOOG
        ("GOOG", "2023-10-24", 2790.0),
        ("GOOG", "2023-10-25", 2795.0),
        ("GOOG", "2023-10-26", 2800.0),
        ("GOOG", "2023-10-27", 2810.0),
        ("GOOG", "2023-10-30", 2798.5),
        # MSFT
        ("MSFT", "2023-10-23", 330.0),
        ("MSFT", "2023-10-24", 332.0),
        ("MSFT", "2023-10-25", 335.0),
        ("MSFT", "2023-10-26", 334.5),
        ("MSFT", "2023-10-27", 336.0),
    ]

    columns = ["stock_symbol", "trade_date", "closing_price"]

    runtime = SparkRuntime()

    df = runtime.spark.createDataFrame(data, columns)
    ex = Ex22(df, runtime=runtime)

    show(ex.solutionWithTempView())
    show(ex.solutionWithPySpark())
