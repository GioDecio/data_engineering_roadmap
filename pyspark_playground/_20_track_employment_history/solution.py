# You are working with an employee dimension table where you need to maintain historical changes
# using Slowly Changing Dimension Type 2 (SCD Type 2). This means that when an employee’s department or designation changes,
# the current record should be marked as inactive and a new row must be added with the updated information.
# Your task is to implement this logic in PySpark by comparing an existing dimension table with new incoming employee records.

from pyspark.sql import SparkSession, Window as W
import pyspark.sql.functions as F
from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType,
    StringType,
    BooleanType,
)
from pyspark_playground.core.utils import show


class Ex20:

    def __init__(self, df_dim, df_incoming):
        self.df_dim = df_dim
        self.df_incoming = df_incoming
        self.today = "2025-07-05"  # Today's date for SCD update
        self.common_columns = ["emp_id", "name", "dept", "designation"]


class JoinSplitUnion(Ex20):

    def track_employment_history(self):
        inc_col = [
            f"inc_{col}" if col != "emp_id" else col for col in self.df_incoming.columns
        ]
        self.df_incoming = self.df_incoming.toDF(*inc_col)

        # Create join table
        join_df = self.df_dim.join(self.df_incoming, on="emp_id", how="full_outer")

        # Create one dataframe per cases: changed, unchanged, new
        changed_df = join_df.filter(
            (
                (F.col("dept") != F.col("inc_dept"))
                | (F.col("designation") != F.col("inc_designation"))
            )
            & (F.col("is_current").isNotNull())
        )

        changed_df = changed_df.withColumn(
            "end_date",
            F.when(F.col("end_date").isNull(), self.today).otherwise(F.col("end_date")),
        )

        changed_old_df = changed_df.select(
            "emp_id",
            "name",
            "dept",
            "designation",
            "is_current",
            "start_date",
            "end_date",
        )
        changed_old_df = changed_old_df.replace(True, False, ["is_current"])

        changed_new_df = changed_df.select(
            "emp_id",
            "inc_name",
            "inc_dept",
            "inc_designation",
            "is_current",
            "start_date",
            "end_date",
        )

        changed_new_df = changed_new_df.withColumnsRenamed(
            {"inc_name": "name", "inc_dept": "dept", "inc_designation": "designation"}
        )

        changed_new_df = changed_new_df.withColumn("start_date", F.lit(self.today))
        changed_new_df = changed_new_df.withColumn("end_date", F.lit(None))

        changed_df = changed_old_df.union(changed_new_df)

        new_df = join_df.filter(F.col("name").isNull())
        new_df = new_df.na.fill({"start_date": self.today}).withColumn(
            "is_current", F.lit(True)
        )
        new_df = new_df.drop("name", "dept", "designation")
        new_df = new_df.withColumnsRenamed(
            {"inc_name": "name", "inc_dept": "dept", "inc_designation": "designation"}
        )

        unchanged_df = join_df.filter(
            (
                (F.col("dept") == F.col("inc_dept"))
                & (F.col("designation") == F.col("inc_designation"))
            )
            | (F.col("inc_name").isNull())
        ).drop("inc_name", "inc_dept", "inc_designation")

        final_cols = [
            "emp_id",
            "name",
            "dept",
            "designation",
            "is_current",
            "start_date",
            "end_date",
        ]
        return (
            new_df.select(final_cols)
            .union(unchanged_df.select(final_cols))
            .union(changed_df.select(final_cols))
        ).orderBy("emp_id")


class UnionDropDupJoin(Ex20):
    def track_employment_history(self):

        # Union of tables
        df_union = (
            self.df_dim.select(self.common_columns)
            .union(self.df_incoming.select(self.common_columns))
            .orderBy("emp_id")
        )

        # Remove duplicates
        df_union = df_union.dropDuplicates(self.common_columns)

        # Join union table with original dimension table
        df_join = (
            df_union.join(
                self.df_dim, on=["emp_id", "name", "dept", "designation"], how="left"
            )
            .na.fill({"start_date": self.today})
            .orderBy("emp_id", F.col("start_date"))
        )

        # Add a ranking columns used to track the size of the group
        w_rank = W.partitionBy("emp_id")
        df_join = df_join.withColumn("rank", F.count("*").over(w_rank))

        # Address "is_current" conditions: If the current value is true and the size of the group is not 1,
        # change to False, otherwise keep that value.
        df_join = df_join.withColumn(
            "is_current",
            F.when(
                (F.col("is_current") == True) & (F.col("rank") != 1), False
            ).otherwise(F.col("is_current")),
        )

        # Address is current for null values setting it to true
        df_join = df_join.withColumn(
            "is_current",
            F.when(F.col("is_current").isNull(), True).otherwise(F.col("is_current")),
        )

        # Address the end date
        df_join = df_join.withColumn(
            "end_date",
            F.when(
                (F.col("rank") == 2) & (F.col("start_date") != self.today), self.today
            ).otherwise(F.col("end_date")),
        )

        # Final DataFrame should be stored in this variable
        return df_join.select(
            "emp_id",
            "name",
            "dept",
            "designation",
            "is_current",
            "start_date",
            "end_date",
        ).orderBy("emp_id", "start_date")


if __name__ == "__main__":

    spark = SparkSession.builder.getOrCreate()

    # Define schema for dimension table
    dim_schema = StructType(
        [
            StructField("emp_id", IntegerType(), False),
            StructField("name", StringType(), True),
            StructField("dept", StringType(), True),
            StructField("designation", StringType(), True),
            StructField("is_current", BooleanType(), True),
            StructField("start_date", StringType(), True),
            StructField("end_date", StringType(), True),
        ]
    )

    # Define schema for incoming updates
    incoming_schema = StructType(
        [
            StructField("emp_id", IntegerType(), False),
            StructField("name", StringType(), True),
            StructField("dept", StringType(), True),
            StructField("designation", StringType(), True),
        ]
    )

    # Sample data
    data_dim = [
        (1, "Alice", "HR", "Analyst", True, "2023-01-01", None),
        (2, "Bob", "Finance", "Manager", True, "2023-01-01", None),
        (3, "Carol", "IT", "Engineer", True, "2023-01-01", None),
        (4, "Dave", "Sales", "Executive", True, "2023-01-01", None),
    ]

    data_incoming = [
        (1, "Alice", "HR", "Sr. Analyst"),
        (2, "Bob", "Finance", "Manager"),
        (4, "Dave", "Marketing", "Executive"),
        (5, "Eve", "IT", "Engineer"),
    ]

    # Create DataFrames with schema
    df_dim = spark.createDataFrame(data_dim, schema=dim_schema)
    df_incoming = spark.createDataFrame(data_incoming, schema=incoming_schema)

    # Show output
    # show(
    #     UnionDropDupJoin(
    #         df_dim, df_incoming
    #     ).track_employment_history_union_drop_duplicates_join()
    # )

    show(JoinSplitUnion(df_dim, df_incoming).track_employment_history())
