# Find the number of stores that each product has been sold in. Import the data from sales_erd.py
from pyspark_playground.core.base import SparkBase
from pyspark_playground.core.runtime import SparkRuntime
from pyspark.sql.functions import (
    col,
    count_distinct,
    sum as spark_sum,
    count,
    regexp_like,
    lit,
)
from pyspark_playground.core.utils import show
from sales_erd import *


class ExC1(SparkBase):

    def __init__(
        self,
        df_store_product_transactions,
        df_products,
        *,
        runtime: SparkRuntime | None = None,
    ):
        super().__init__(runtime=runtime)
        self.df_store_product_transactions = df_store_product_transactions
        self.df_products = df_products

    def _join_df(self):

        return self.df_store_product_transactions.join(
            self.df_products, on="product_id", how="left"
        )

    def solutionWithTempView(self):

        self.df_store_product_transactions.createOrReplaceTempView(
            "store_product_transactions"
        )
        self.df_products.createOrReplaceTempView("products")

        query = """
        SELECT P.name AS ProductName
                , count(DISTINCT store_id) cnt
        FROM store_product_transactions SPT
        LEFT JOIN products AS P ON P.product_id = SPT.product_id 
        GROUP BY P.name
        """

        return self.spark.sql(query)

    def solutionWithTempViewNoDistinct(self):

        self.df_store_product_transactions.createOrReplaceTempView(
            "store_product_transactions"
        )
        self.df_products.createOrReplaceTempView("products")

        query = """
            with deduped AS (
            SELECT product_id
                   , store_id
            FROM store_product_transactions 
            GROUP BY 1, 2
            )
            SELECT P.name AS ProductName
                , count(*) cnt
            FROM deduped SPT
            LEFT JOIN products AS P ON P.product_id = SPT.product_id 
            GROUP BY P.name
        """

        show(self.spark.sql("""SELECT product_id
                   , store_id
            FROM store_product_transactions 
            GROUP BY 1, 2"""))

        return self.spark.sql(query)

    def solutionWithPySpark(self):

        df = self._join_df()

        return df.groupBy(col("name").alias("ProductName")).agg(
            count_distinct(col("store_id")).alias("cnt")
        )

    def solutionWithDropDuplicates(self):

        df = self._join_df()

        df = df.dropDuplicates(["product_id", "store_id"])

        return df.groupBy(col("name").alias("ProductName")).agg(count("*").alias("cnt"))

    def solutionWithPySpark2(self):

        df = self._join_df()

        return df.groupBy(col("name").alias("ProductName")).agg(
            count_distinct(col("store_id")).alias("cnt"),
            spark_sum(col("active_flag")).alias("dummy"),
        )

    def solutionWithPySpark3(self):

        df = self._join_df()

        return df.groupBy(col("name").alias("ProductName")).agg({"active_flag": "sum"})


if __name__ == "__main__":

    runtime = SparkRuntime()

    df_store_product_transactions = runtime.spark.createDataFrame(
        store_product_transactions_data, store_product_transactions_schema
    )
    df_products = runtime.spark.createDataFrame(products_data, products_schema)

    ex = ExC1(df_store_product_transactions, df_products, runtime=runtime)

    # show(ex.solutionWithPySpark())
    # show(ex.solutionWithPySpark2())
    # show(ex.solutionWithPySpark3())
    # show(ex.solutionWithTempView())
    # show(ex.solutionWithDropDuplicates())
    show(ex.solutionWithTempViewNoDistinct())

    test_df = ex.solutionWithTempViewNoDistinct().filter(
        regexp_like(col("ProductName"), lit("^Wire"))
    )

    test_values_rows = test_df.collect()
    test_values = [row["cnt"] for row in test_values_rows]

    print(assert test_values == [3])
