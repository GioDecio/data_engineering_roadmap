import importlib.util
import sys
import pytest
from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DoubleType, IntegerType
from params_pyspark_playground import (
    EX1_PARAMS, EX2_PARAMS, EX3_PARAMS, EX4_EMPLOYEES, EX4_PARAMS,
    EX5_PARAMS, PLAYERS_DATA, COUNTRIES_DATA, EX13_EXPECTED_NAMES,
    EX14_PARAMS, EX15_PARAMS, EX16_PRODUCTS, EX16_PARAMS, EX17_PARAMS,
)


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


ex1  = _load("ex1",  "pyspark_playground/1_e_load_and_transform_data.py")
ex2  = _load("ex2",  "pyspark_playground/2_e_handling_null_values.py")
ex3  = _load("ex3",  "pyspark_playground/3_e_total_purchase_py_customer.py")
ex4  = _load("ex4",  "pyspark_playground/4_m_running_payroll.py")
ex5  = _load("ex5",  "pyspark_playground/5_m_food_beverage_and_sales.py")
ex7  = _load("ex7",  "pyspark_playground/7_m_load_and-transform_json_files.py")
ex13 = _load("ex13", "pyspark_playground/13_h_top_players.py")
ex13r = _load("ex13r", "pyspark_playground/13_h_top_players_regex.py")
ex14 = _load("ex14", "pyspark_playground/14_e_daily_total_sales.py")
ex15 = _load("ex15", "pyspark_playground/15_m_top_5_by_day.py")
ex16 = _load("ex16", "pyspark_playground/16_h_products_w_increasing_sales.py")
ex17 = _load("ex17", "pyspark_playground/17_m_remove_outliers_from_trip.py")


# --- Exercise 1 ---

@pytest.mark.parametrize("data, expected_ids", EX1_PARAMS)
def test_filter_customers(spark, data, expected_ids):
    df = spark.createDataFrame(data, ["customer_id", "name", "email", "age", "purchase_amount"])
    result_ids = {row.customer_id for row in ex1.filter_customers(df).collect()}
    assert result_ids == expected_ids


# --- Exercise 2 ---

@pytest.mark.parametrize("data, expected_ids", EX2_PARAMS)
def test_filter_null_values(spark, data, expected_ids):
    df = spark.createDataFrame(data, ["customer_id", "email"])
    result_ids = {row.customer_id for row in ex2.filter_null_values(df).collect()}
    assert result_ids == expected_ids


# --- Exercise 3 ---

@pytest.mark.parametrize("data, expected", EX3_PARAMS)
def test_total_purchase_by_customer(spark, data, expected):
    df = spark.createDataFrame(data, ["customer_id", "purchase_amount"])
    result = {row.customer_id: row.total_purchase for row in ex3.total_purchase_by_customer(df).collect()}
    assert result == expected


# --- Exercise 4 ---

@pytest.mark.parametrize("payroll_data, expected_pay", EX4_PARAMS)
def test_calculate_payroll(spark, payroll_data, expected_pay):
    employees = spark.createDataFrame(EX4_EMPLOYEES, ["employee_id", "name", "position"])
    payroll = spark.createDataFrame(payroll_data, ["employee_id", "hours_worked", "hourly_rate"])
    result = {row.employee_id: row.pay for row in ex4.calculate_payroll(employees, payroll).collect()}
    assert result == expected_pay


# --- Exercise 5 ---

@pytest.mark.parametrize("products_data, sales_data, inventory_data, expected", EX5_PARAMS)
def test_food_beverage_sales(spark, products_data, sales_data, inventory_data, expected):
    products  = spark.createDataFrame(products_data, ["product_id", "name", "category"])
    sales     = spark.createDataFrame(sales_data, ["product_id", "quantity", "revenue"])
    inventory = spark.createDataFrame(inventory_data, ["product_id", "stock"])
    result = {
        row.product_id: (row.total_quantity, row.total_revenue)
        for row in ex5.food_beverage_sales(products, sales, inventory).collect()
    }
    assert result == expected


# --- Exercise 7 ---

def test_transform_orders(spark):
    schema = StructType([
        StructField("customer_id", IntegerType()),
        StructField("order_id", IntegerType()),
        StructField("products", ArrayType(StructType([
            StructField("product_name", StringType()),
            StructField("product_price", DoubleType()),
        ]))),
    ])
    data = [
        (1, 100, [{"product_name": "Widget", "product_price": 9.99},
                  {"product_name": "Gadget", "product_price": 14.99}]),
        (2, 101, [{"product_name": "Doohickey", "product_price": 4.99}]),
    ]
    df = spark.createDataFrame(data, schema)
    result = ex7.transform_orders(df).collect()
    assert len(result) == 3
    names = {row.product_name for row in result}
    assert names == {"Widget", "Gadget", "Doohickey"}


# --- Exercise 13 ---

@pytest.mark.parametrize("func", [ex13.top_players, ex13r.top_players_regex])
def test_top_players(spark, func):
    players_df  = spark.createDataFrame(PLAYERS_DATA, ["player", "runs", "50s/100s"])
    countries_df = spark.createDataFrame(COUNTRIES_DATA, ["SRT", "country"])
    result = [row.playername for row in func(players_df, countries_df).collect()]
    assert result == EX13_EXPECTED_NAMES


# --- Exercise 14 ---

@pytest.mark.parametrize("data, expected", EX14_PARAMS)
def test_daily_total_sales(spark, data, expected):
    df = spark.createDataFrame(data, ["store_id", "product_id", "sale_date", "quantity_sold", "total_sales"])
    result = {
        (row.store_id, row.sale_date): row["sum(total_sales)"]
        for row in ex14.daily_total_sales(df).collect()
    }
    assert result == expected


# --- Exercise 15 ---

@pytest.mark.parametrize("data, expected", EX15_PARAMS)
def test_top_5_by_day(spark, data, expected):
    df = spark.createDataFrame(data, ["store_id", "product_id", "sale_date", "quantity_sold", "total_sales"])
    result = {}
    for row in ex15.top_5_by_day(df).collect():
        result.setdefault(row.sale_date, set()).add(row.product_id)
    assert result == expected


# --- Exercise 16 ---

@pytest.mark.parametrize(
    "func",
    [
        ex16.products_with_increasing_sales_with_coalesce,
        ex16.products_with_increasing_sales_distinct,
        ex16.products_with_increasing_sales_groupby,
        ex16.products_with_increasing_sales_rdd,
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
        ex17.remove_outliers_from_trip,
        ex17.remove_outliers_from_trip_improved,
        lambda df: ex17.remove_outliers_generic(df, ["trip_cost", "rating"]),
    ],
)
@pytest.mark.parametrize("trip_data, expected_ids", EX17_PARAMS)
def test_remove_outliers(spark, func, trip_data, expected_ids):
    df = spark.createDataFrame(trip_data, ["trip_id", "trip_cost", "rating"])
    result_ids = {row.trip_id for row in func(df).collect()}
    assert result_ids == expected_ids
