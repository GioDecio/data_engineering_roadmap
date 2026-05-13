from pyspark.sql import SparkSession, DataFrame
from pyspark.sql import functions as F
from pyspark_playground.utils import show

spark = SparkSession.builder.appName("Spark Playground").getOrCreate()


def food_beverage_sales(
    products: DataFrame, sales: DataFrame, inventory: DataFrame
) -> DataFrame:
    tot_sale_rev = sales.groupBy("product_id").agg(
        F.sum("quantity").alias("total_quantity"),
        F.sum("revenue").alias("total_revenue"),
    )
    tot_stock = inventory.groupBy("product_id").agg(F.sum("stock").alias("total_stock"))
    return (
        products.join(tot_sale_rev, on="product_id", how="left")
        .join(tot_stock, on="product_id", how="left")
        .select("category", "name", "product_id", "total_quantity", "total_revenue", "total_stock")
        .orderBy("category")
        .fillna({"total_quantity": 0, "total_revenue": 0, "total_stock": 0})
    )


if __name__ == "__main__":
    products_data = [(1, "Coffee", "Beverage"), (2, "Sandwich", "Food"), (3, "Juice", "Beverage")]
    sales_data = [(1, 10, 50.0), (2, 5, 25.0)]
    inventory_data = [(1, 100), (2, 50), (3, 80)]

    products = spark.createDataFrame(products_data, ["product_id", "name", "category"])
    sales = spark.createDataFrame(sales_data, ["product_id", "quantity", "revenue"])
    inventory = spark.createDataFrame(inventory_data, ["product_id", "stock"])
    show(food_beverage_sales(products, sales, inventory))
