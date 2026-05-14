import pytest
from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    ArrayType,
    DoubleType,
    IntegerType,
)
from params_pyspark_playground import *
from pyspark_playground import *

# --- Exercise 1 ---


@pytest.mark.parametrize("data, expected_ids", EX1_PARAMS)
def test_filter_customers(spark, data, expected_ids):
    df = spark.createDataFrame(
        data, ["customer_id", "name", "email", "age", "purchase_amount"]
    )
    result_ids = {row.customer_id for row in filter_customers(df).collect()}
    assert result_ids == expected_ids


# --- Exercise 2 ---


@pytest.mark.parametrize("data, expected_ids", EX2_PARAMS)
def test_filter_null_values(spark, data, expected_ids):
    df = spark.createDataFrame(data, ["customer_id", "email"])
    result_ids = {row.customer_id for row in filter_null_values(df).collect()}
    assert result_ids == expected_ids


# --- Exercise 3 ---


@pytest.mark.parametrize("data, expected", EX3_PARAMS)
def test_total_purchase_by_customer(spark, data, expected):
    df = spark.createDataFrame(data, ["customer_id", "purchase_amount"])
    result = {
        row.customer_id: row.total_purchase
        for row in total_purchase_by_customer(df).collect()
    }
    assert result == expected


# --- Exercise 4 ---


@pytest.mark.parametrize("payroll_data, expected_pay", EX4_PARAMS)
def test_calculate_payroll(spark, payroll_data, expected_pay):
    employees = spark.createDataFrame(
        EX4_EMPLOYEES, ["employee_id", "name", "position"]
    )
    payroll = spark.createDataFrame(
        payroll_data, ["employee_id", "hours_worked", "hourly_rate"]
    )
    result = {
        row.employee_id: row.pay
        for row in calculate_payroll(employees, payroll).collect()
    }
    assert result == expected_pay


# --- Exercise 5 ---


@pytest.mark.parametrize(
    "products_data, sales_data, inventory_data, expected", EX5_PARAMS
)
def test_food_beverage_sales(
    spark, products_data, sales_data, inventory_data, expected
):
    products = spark.createDataFrame(products_data, ["product_id", "name", "category"])
    sales = spark.createDataFrame(sales_data, ["product_id", "quantity", "revenue"])
    inventory = spark.createDataFrame(inventory_data, ["product_id", "stock"])
    result = {
        row.product_id: (row.total_quantity, row.total_revenue)
        for row in food_beverage_sales(products, sales, inventory).collect()
    }
    assert result == expected


# --- Exercise 7 ---


def test_transform_orders(spark):
    schema = StructType(
        [
            StructField("customer_id", IntegerType()),
            StructField("order_id", IntegerType()),
            StructField(
                "products",
                ArrayType(
                    StructType(
                        [
                            StructField("product_name", StringType()),
                            StructField("product_price", DoubleType()),
                        ]
                    )
                ),
            ),
        ]
    )
    data = [
        (
            1,
            100,
            [
                {"product_name": "Widget", "product_price": 9.99},
                {"product_name": "Gadget", "product_price": 14.99},
            ],
        ),
        (2, 101, [{"product_name": "Doohickey", "product_price": 4.99}]),
    ]
    df = spark.createDataFrame(data, schema)
    result = transform_orders(df).collect()
    assert len(result) == 3
    names = {row.product_name for row in result}
    assert names == {"Widget", "Gadget", "Doohickey"}


# --- Exercise 13 ---


@pytest.mark.parametrize("func", [top_players, top_players_regex])
def test_top_players(spark, func):
    players_df = spark.createDataFrame(
        EX13_PLAYERS_DATA, ["player", "runs", "50s/100s"]
    )
    countries_df = spark.createDataFrame(EX13_COUNTRIES_DATA, ["SRT", "country"])
    result = [row.playername for row in func(players_df, countries_df).collect()]
    assert result == EX13_EXPECTED_NAMES


# --- Exercise 14 ---


@pytest.mark.parametrize("data, expected", EX14_PARAMS)
def test_daily_total_sales(spark, data, expected):
    df = spark.createDataFrame(
        data, ["store_id", "product_id", "sale_date", "quantity_sold", "total_sales"]
    )
    result = {
        (row.store_id, row.sale_date): row["sum(total_sales)"]
        for row in daily_total_sales(df).collect()
    }
    assert result == expected


# --- Exercise 15 ---


@pytest.mark.parametrize("data, expected", EX15_PARAMS)
def test_top_5_by_day(spark, data, expected):
    df = spark.createDataFrame(
        data, ["store_id", "product_id", "sale_date", "quantity_sold", "total_sales"]
    )
    result = {}
    for row in top_5_by_day(df).collect():
        result.setdefault(row.sale_date, set()).add(row.product_id)
    assert result == expected


# --- Exercise 16 ---


@pytest.mark.parametrize(
    "func",
    [
        products_with_increasing_sales_with_coalesce,
        products_with_increasing_sales_distinct,
        products_with_increasing_sales_groupby,
        products_with_increasing_sales_rdd,
    ],
)
@pytest.mark.parametrize("sales_data, expected_ids", EX16_PARAMS)
def test_products_with_increasing_sales(spark, func, sales_data, expected_ids):
    df_products = spark.createDataFrame(EX16_PRODUCTS, ["product_id", "product_name"])
    df_sales = spark.createDataFrame(sales_data, ["product_id", "year", "revenue"])
    result_ids = {row.product_id for row in func(df_products, df_sales).collect()}
    assert result_ids == expected_ids


# --- Exercise 17 ---
@pytest.mark.parametrize(
    "func",
    [
        remove_outliers_from_trip,
        remove_outliers_from_trip_improved,
        lambda df: remove_outliers_generic(df, ["trip_cost", "rating"]),
    ],
)
@pytest.mark.parametrize("trip_data, expected_ids", EX17_PARAMS)
def test_remove_outliers(spark, func, trip_data, expected_ids):
    df = spark.createDataFrame(trip_data, ["trip_id", "trip_cost", "rating"])
    result_ids = {row.trip_id for row in func(df).collect()}
    assert result_ids == expected_ids


# --- Exercise 18 ---
@pytest.mark.parametrize(
    "func",
    [driver_details_for_riders],
)
@pytest.mark.parametrize("rides_data, drivers_data, expected_ids", EX18_PARAMS)
def test_driver_details_for_riders(spark, func, rides_data, drivers_data, expected_ids):
    rides_df = spark.createDataFrame(
        rides_data, ["ride_id", "driver_id", "fare_amount"]
    )
    drivers_df = spark.createDataFrame(
        drivers_data, ["driver_id", "driver_name", "status"]
    )
    result_ids = {row.ride_id for row in func(rides_df, drivers_df).collect()}
    assert result_ids == expected_ids


# --- Exercise 19 ---


@pytest.mark.parametrize(
    "func",
    [customer_loyalty_score],
)
@pytest.mark.parametrize(
    "rides_data, payment_types_data, ratings_data, customers_data, expected",
    EX19_PARAMS,
)
def test_customer_loyalty_score(
    spark, func, rides_data, payment_types_data, ratings_data, customers_data, expected
):
    rides_df = spark.createDataFrame(
        rides_data, ["trip_id", "customer_id", "payment_type_id"]
    )
    payment_types_df = spark.createDataFrame(
        payment_types_data, ["payment_type_id", "payment_type"]
    )
    ratings_df = spark.createDataFrame(ratings_data, ["trip_id", "rating"])
    customers_df = spark.createDataFrame(customers_data, ["customer_id", "name"])
    result = {
        (row.customer_id, row.customer_name, row.loyalty_score)
        for row in func(rides_df, payment_types_df, ratings_df, customers_df).collect()
    }
    assert result == expected


# --- Exercise 20 ---


@pytest.mark.parametrize("cls", [UnionDropDupJoin, JoinSplitUnion])
@pytest.mark.parametrize("dim_data, dim_incoming_data, expected", EX20_PARAMS)
def test_track_employment_history(spark, cls, dim_data, dim_incoming_data, expected):

    dim_df = spark.createDataFrame(dim_data, schema=EX20_DIM_SCHEMA)
    dim_incoming_df = spark.createDataFrame(
        dim_incoming_data, schema=EX20_INCOMING_SCHEMA
    )

    result = {
        (
            row.emp_id,
            row.name,
            row.dept,
            row.designation,
            row.is_current,
            row.start_date,
            row.end_date,
        )
        for row in cls(dim_df, dim_incoming_df)
        .track_employment_history()
        .filter(col("emp_id") == 1)
        .collect()
    }

    assert result == expected


@pytest.mark.parametrize("cls", [UnionDropDupJoin, JoinSplitUnion])
@pytest.mark.parametrize("dim_data, dim_incoming_data, expected", EX20_PARAMS)
def test_track_employment_history_properties(
    spark, cls, dim_data, dim_incoming_data, expected
):

    dim_df = spark.createDataFrame(dim_data, schema=EX20_DIM_SCHEMA)
    dim_incoming_df = spark.createDataFrame(
        dim_incoming_data, schema=EX20_INCOMING_SCHEMA
    )

    result_df = cls(dim_df, dim_incoming_df).track_employment_history()

    # Changed records must be closed: end_date set
    for row in result_df.filter(col("is_current") == False).collect():
        assert row.end_date is not None

    # New records (not in dim) must be active
    dim_ids = {row.emp_id for row in dim_df.collect()}
    incoming_ids = {row.emp_id for row in dim_incoming_df.collect()}
    for row in result_df.filter(col("emp_id").isin(incoming_ids - dim_ids)).collect():
        assert row.is_current == True

    # Unchanged records (in dim but not in incoming) must remain active
    for row in result_df.filter(col("emp_id").isin(dim_ids - incoming_ids)).collect():
        assert row.is_current == True
        assert row.end_date is None
