from pyspark.sql.types import (
    StructField,
    StructType,
    IntegerType,
    StringType,
    FloatType,
)

departments_data = [
    (1, "Food & Drink"),
    (2, "Clothing"),
    (3, "Electronics"),
    (4, "Home & Garden"),
    (5, "Beauty"),
]

stores_data = [
    (1, "M&S Manchester Arndale", "2005-03-15"),
    (2, "M&S London Oxford St", "1998-09-01"),
    (3, "M&S Edinburgh Princes St", "2010-06-20"),
    (4, "M&S Cardiff Queens St", "2008-11-10"),
    (5, "M&S Belfast Victoria Sq", "2012-04-05"),
]

products_schema = StructType(
    [
        StructField("product_id", IntegerType(), False),
        StructField("name", StringType(), True),
        StructField("department_id", IntegerType(), True),
        StructField("created_date", StringType(), True),
        StructField("active_flag", IntegerType(), True),
    ]
)


stores_schema = StructType(
    [
        StructField("store_id", IntegerType(), False),
        StructField("store_name", StringType()),
        StructField("open_date", StringType()),
    ]
)

department_schema = StructType(
    [
        StructField("department_id", IntegerType(), False),
        StructField("department_name", StringType(), True),
    ]
)

products_data = [
    (1, "Per Una Midi Dress", 2, "2020-01-10", 1),
    (2, "M&S Select Whisky", 1, "2019-05-22", 1),
    (3, "Cashmere Crew Neck", 2, "2021-03-15", 1),
    (4, "Plant Kitchen Burger", 1, "2022-07-01", 1),
    (5, "Egyptian Cotton Bedset", 4, "2018-11-30", 1),
    (6, "Wireless Earbuds", 3, "2023-02-14", 1),
    (7, "Rose Gold Moisturiser", 5, "2020-09-09", 1),
    (8, "Classic Chino Trousers", 2, "2017-06-25", 0),
    (9, "Sparks Loyalty Card", 1, "2021-01-01", 1),
    (10, "Autograph Wool Coat", 2, "2022-10-03", 1),
]

product_price_history_data = [
    (1, "2020-01-10", 45.00),
    (1, "2023-06-01", 49.00),
    (2, "2019-05-22", 22.00),
    (2, "2024-01-01", 25.00),
    (3, "2021-03-15", 89.00),
    (3, "2024-03-01", 95.00),
    (4, "2022-07-01", 4.50),
    (5, "2018-11-30", 79.00),
    (5, "2022-09-01", 85.00),
    (6, "2023-02-14", 35.00),
    (7, "2020-09-09", 18.00),
    (7, "2023-11-01", 20.00),
    (8, "2017-06-25", 35.00),
    (9, "2021-01-01", 0.00),
    (10, "2022-10-03", 159.00),
    (10, "2024-10-01", 175.00),
]

product_price_history_schema = StructType(
    [
        StructField("product_id", IntegerType(), False),
        StructField("effective_date", StringType(), True),
        StructField("price", FloatType(), True),
    ]
)

store_product_transactions_data = [
    (1, 1, "2024-01-15"),
    (3, 1, "2024-02-20"),
    (6, 1, "2024-03-05"),
    (10, 1, "2024-04-18"),
    (2, 1, "2024-05-30"),
    (1, 2, "2024-01-20"),
    (2, 2, "2024-02-14"),
    (4, 2, "2024-03-22"),
    (7, 2, "2024-04-09"),
    (9, 2, "2024-06-01"),
    (3, 3, "2024-01-08"),
    (5, 3, "2024-02-28"),
    (8, 3, "2024-03-17"),
    (10, 3, "2024-05-05"),
    (2, 4, "2024-01-25"),
    (4, 4, "2024-03-30"),
    (6, 4, "2024-04-14"),
    (1, 5, "2024-02-10"),
    (7, 5, "2024-03-25"),
    (9, 5, "2024-05-15"),
    (1, 3, "2024-06-10"),
    (1, 4, "2024-06-15"),
    (3, 2, "2024-07-01"),
    (6, 2, "2024-07-20"),
]

store_product_transactions_schema = StructType(
    [
        StructField("product_id", IntegerType(), False),
        StructField("store_id", IntegerType(), False),
        StructField("transaction_date", StringType(), True),
    ]
)
