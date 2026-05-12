import re
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import Window as W

spark = SparkSession.builder.appName("Spark Playground").getOrCreate()

# Assume the dataframes products, sales, inventory are already initialized.

# Write the logic and display the final dataframe

tot_sale_rev = sales.groupBy("product_id").agg(
    F.sum("quantity").alias("total_quantity"), F.sum("revenue").alias("total_revenue")
)

tot_stock = inventory.groupBy("product_id").agg(F.sum("stock").alias("total_stock"))

df_all = products.join(tot_sale_rev, on="product_id", how="left").join(
    tot_stock, on="product_id", how="left"
)


# _dict = {head:0 for head in df_all.columns if re.search('^tot',head)}
_dict = dict.fromkeys(["total_quantity", "total_revenue", "total_stock"], 0)

df_result = (
    df_all.select(
        "category",
        "name",
        "product_id",
        "total_quantity",
        "total_revenue",
        "total_stock",
    )
    .orderBy("category")
    .fillna(_dict)
)

display(df_result)
