import pytest

# Exercise 1 — filter_customers
# (customer_id, name, email, age, purchase_amount)
# keep: purchase_amount > 100 AND age >= 30

EX1_PARAMS = [
    pytest.param(
        [
            (1, "Alice", "a@x.com", 35, 150.0),  # ✓
            (2, "Bob", "b@x.com", 25, 200.0),  # age < 30 ✗
            (3, "Carol", "c@x.com", 40, 80.0),  # amount <= 100 ✗
            (4, "Dave", "d@x.com", 30, 101.0),
        ],  # ✓
        {1, 4},
        id="mixed",
    ),
    pytest.param(
        [
            (1, "Alice", "a@x.com", 30, 100.0),  # amount not > 100 ✗
            (2, "Bob", "b@x.com", 29, 200.0),
        ],  # age < 30 ✗
        set(),
        id="none_pass",
    ),
]

# Exercise 2 — filter_null_values
# (customer_id, email) — keep rows where both are non-null

EX2_PARAMS = [
    pytest.param(
        [(1, "a@x.com"), (2, None), (None, "c@x.com"), (4, "d@x.com")],
        {1, 4},
        id="mixed_nulls",
    ),
    pytest.param(
        [(1, "a@x.com"), (2, "b@x.com")],
        {1, 2},
        id="no_nulls",
    ),
]

# Exercise 3 — total_purchase_by_customer
# (customer_id, purchase_amount) → (customer_id, total_purchase)

EX3_PARAMS = [
    pytest.param(
        [(1, 100.0), (1, 50.0), (2, 200.0), (2, 75.0)],
        {1: 150.0, 2: 275.0},
        id="two_customers",
    ),
    pytest.param(
        [(1, 100.0), (2, 200.0), (3, 300.0)],
        {1: 100.0, 2: 200.0, 3: 300.0},
        id="single_purchases",
    ),
]

# Exercise 4 — calculate_payroll
# employees: (employee_id, name, position)
# payroll:   (employee_id, hours_worked, hourly_rate)
# pay = hours * rate if hours <= 40 else 40*rate + (hours-40)*rate*1.5

EX4_EMPLOYEES = [
    (1, "Alice", "Engineer"),
    (2, "Bob", "Manager"),
    (3, "Carol", "Analyst"),
]

EX4_PARAMS = [
    pytest.param(
        [
            (1, 38.0, 50.0),  # no overtime: 38*50 = 1900
            (2, 45.0, 60.0),  # overtime:    40*60 + 5*60*1.5 = 2850
            (3, 40.0, 40.0),
        ],  # exactly 40:  40*40 = 1600
        {1: 1900.0, 2: 2850.0, 3: 1600.0},
        id="mixed_overtime",
    ),
]

# Exercise 5 — food_beverage_sales
# products:  (product_id, name, category)
# sales:     (product_id, quantity, revenue)
# inventory: (product_id, stock)
# product with no sales → total_quantity=0, total_revenue=0

EX5_PARAMS = [
    pytest.param(
        [(1, "Coffee", "Beverage"), (2, "Sandwich", "Food"), (3, "Juice", "Beverage")],
        [(1, 10, 50.0), (2, 5, 25.0)],
        [(1, 100), (2, 50), (3, 80)],
        {1: (10, 50.0), 2: (5, 25.0), 3: (0, 0)},
        id="one_product_no_sales",
    ),
]

# Exercise 13 — top_players / top_players_regex
# players:   (player "Name-CODE", runs, "50s/100s")
# countries: (SRT, country)
# keep sum(50s + 100s) > 95, sorted by runs desc

EX13_PLAYERS_DATA = [
    ("Sachin-IND", 18694, "93/49"),  # sum=142 ✓
    ("Ricky-AUS", 11274, "66/31"),  # sum=97  ✓
    ("Lara-WI", 10222, "45/21"),  # sum=66  ✗
    ("Rahul-IND", 10355, "95/11"),  # sum=106 ✓
    ("Jhonnty-SA", 7051, "43/5"),  # sum=48  ✗
    ("Hayden-AUS", 8722, "67/19"),  # sum=86  ✗
]
EX13_COUNTRIES_DATA = [
    ("IND", "India"),
    ("AUS", "Australia"),
    ("WI", "WestIndies"),
    ("SA", "SouthAfrica"),
]

EX13_EXPECTED_NAMES = ["Sachin", "Ricky", "Rahul"]  # sorted by runs desc

# Exercise 14 — daily_total_sales
# (store_id, product_id, sale_date, quantity_sold, total_sales)
# → groupBy(store_id, sale_date).sum(total_sales)

EX14_PARAMS = [
    pytest.param(
        [
            (1, 101, "2025-05-10", 2, 25.0),
            (1, 102, "2025-05-10", 1, 15.0),
            (1, 103, "2025-05-11", 3, 30.0),
            (2, 101, "2025-05-10", 2, 40.0),
        ],
        {(1, "2025-05-10"): 40.0, (1, "2025-05-11"): 30.0, (2, "2025-05-10"): 40.0},
        id="two_stores_two_days",
    ),
]

# Exercise 15 — top_5_by_day
# same schema as ex14
# → top 5 products by total_sales per sale_date

EX15_PARAMS = [
    pytest.param(
        [
            (1, 101, "2025-05-10", 1, 25.0),
            (1, 102, "2025-05-10", 1, 50.0),
            (1, 103, "2025-05-10", 1, 30.0),
            (1, 104, "2025-05-10", 1, 45.0),
            (1, 105, "2025-05-10", 1, 60.0),
            (1, 106, "2025-05-10", 1, 10.0),
        ],  # 6 products → 106 excluded
        {"2025-05-10": {101, 102, 103, 104, 105}},
        id="six_products_one_excluded",
    ),
]

# Exercise 16 — products with increasing sales
EX16_PRODUCTS = [(1, "A"), (2, "B"), (3, "C")]

EX16_PARAMS = [
    pytest.param(
        [
            (1, 2022, 100.0),
            (1, 2023, 200.0),
            (2, 2022, 300.0),
            (2, 2023, 200.0),
            (3, 2022, 100.0),
            (3, 2023, 100.0),
        ],
        {1},
        id="standard",
    ),
    pytest.param(
        [(1, 2022, 100.0), (1, 2023, 200.0), (2, 2022, 300.0), (2, 2023, 200.0)],
        {1},
        id="two_products",
    ),
    pytest.param(
        [
            (1, 2022, 100.0),
            (1, 2023, 200.0),
            (2, 2022, 100.0),
            (2, 2023, 200.0),
            (3, 2022, 100.0),
            (3, 2023, 200.0),
        ],
        {1, 2, 3},
        id="all_increasing",
    ),
    pytest.param(
        [
            (1, 2022, 500.0),
            (1, 2023, 100.0),
            (2, 2022, 500.0),
            (2, 2023, 100.0),
            (3, 2022, 500.0),
            (3, 2023, 100.0),
        ],
        set(),
        id="all_decreasing",
    ),
]

# Exercise 17 — remove outliers
EX17_PARAMS = [
    pytest.param(
        [
            (1, 10.0, 4.0),
            (2, 10.0, 4.0),
            (3, 11.0, 4.0),
            (4, 11.0, 4.0),
            (5, 12.0, 4.0),
            (6, 12.0, 4.0),
            (7, 13.0, 4.0),
            (8, 13.0, 4.0),
            (9, 100.0, 4.0),
        ],
        {1, 2, 3, 4, 5, 6, 7, 8},
        id="one_trip_cost_outlier",
    ),
    pytest.param(
        [
            (1, 10.0, 4.0),
            (2, 10.0, 4.0),
            (3, 11.0, 4.0),
            (4, 11.0, 4.0),
            (5, 12.0, 4.0),
            (6, 12.0, 4.0),
            (7, 13.0, 4.0),
            (8, 13.0, 4.0),
        ],
        {1, 2, 3, 4, 5, 6, 7, 8},
        id="no_outliers",
    ),
]


EX18_PARAMS = [
    pytest.param(
        [(1, 101, 10.0), (2, 102, 20.0), (3, 103, 30.0)],
        [
            (101, "Alex", "available"),
            (102, "Sam", "off_duty"),
            (103, "Rita", "available"),
        ],
        {1, 2, 3},
        id="all_drivers_present",
    ),
]


EX19_PARAMS = [
    pytest.param(
        [
            (1, 101, 1),
            (2, 102, 2),
            (3, 101, 1),
            (4, 103, 3),
            (5, 104, 1),
            (6, 102, 3),
            (7, 101, 2),
            (8, 105, 3),
            (9, 106, 1),
            (10, 107, 2),
            (11, 108, 1),
            (12, 103, 1),
        ],
        [(1, "Card"), (2, "Cash"), (3, "Ryd credits")],
        [(1, 4.5), (3, 3.0), (4, 5.0), (6, 4.0), (8, 4.8), (10, 3.7), (12, 4.1)],
        [
            (101, "Alice"),
            (102, "Bob"),
            (103, "Carol"),
            (104, "David"),
            (105, "Eva"),
            (106, "Frank"),
            (107, "Grace"),
            (108, "Helen"),
            (109, "Ivy"),
        ],
        {
            (101, "Alice", 30),
            (103, "Carol", 30),
            (102, "Bob", 15),
            (105, "Eva", 15),
            (104, "David", 10),
            (106, "Frank", 10),
            (107, "Grace", 0),
            (108, "Helen", 10),
            (109, "Ivy", 0),
        },
        id="basic",
    ),
]
