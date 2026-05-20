from pyspark_playground.core.base import SparkBase
from pyspark_playground.core.runtime import SparkRuntime
from pyspark.sql.functions import col
from pyspark_playground.core.utils import show
from pyspark.sql import DataFrame


class Ex1(SparkBase):

    def __init__(self, runtime: SparkRuntime, df):
        super().__init__(runtime=runtime)
        self.df = df

    def filter_customers(self) -> DataFrame:
        return (
            self.df.filter(col("purchase_amount") > 100)
            .filter(col("age") >= 30)
            .select("customer_id", "name", "purchase_amount")
        )


if __name__ == "__main__":
    FILEPATH = "pyspark_playground/datasets/customers.csv"
    runtime = SparkRuntime()
    df = runtime.spark.read.csv(path=FILEPATH, inferSchema=True, header=True)
    ex = Ex1(runtime, df)

    show(ex.filter_customers())
