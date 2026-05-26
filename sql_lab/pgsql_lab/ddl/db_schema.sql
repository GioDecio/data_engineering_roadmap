-- ============================================================
-- DDL
-- ============================================================

CREATE TABLE departments (
    department_id   INTEGER         PRIMARY KEY,
    department_name VARCHAR(100)    NOT NULL
);

CREATE TABLE products (
    product_id      INTEGER         PRIMARY KEY,
    name            VARCHAR(100)    NOT NULL,
    department_id   INTEGER         NOT NULL,
    created_date    DATE            NOT NULL,
    active_flag     INT             NOT NULL,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

CREATE TABLE stores (
    store_id        INTEGER         PRIMARY KEY,
    store_name      VARCHAR(100)    NOT NULL,
    open_date       DATE            NOT NULL
);

CREATE TABLE store_product_transactions (
    product_id          INTEGER     NOT NULL,
    store_id            INTEGER     NOT NULL,
    transaction_date    DATE        NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (store_id)   REFERENCES stores(store_id)
);

CREATE TABLE product_price_history (
    product_id      INTEGER         NOT NULL,
    effective_date  DATE            NOT NULL,
    price           DECIMAL(10, 2)  NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);


-- ============================================================
-- INSERT INTO
-- ============================================================

INSERT INTO departments (department_id, department_name) VALUES
(1, 'Food & Drink'),
(2, 'Clothing'),
(3, 'Electronics'),
(4, 'Home & Garden'),
(5, 'Beauty');

INSERT INTO stores (store_id, store_name, open_date) VALUES
(1, 'M&S Manchester Arndale',  '2005-03-15'),
(2, 'M&S London Oxford St',    '1998-09-01'),
(3, 'M&S Edinburgh Princes St','2010-06-20'),
(4, 'M&S Cardiff Queens St',   '2008-11-10'),
(5, 'M&S Belfast Victoria Sq', '2012-04-05');

INSERT INTO products (product_id, name, department_id, created_date, active_flag) VALUES
(1,  'Per Una Midi Dress',       2, '2020-01-10', 1),
(2,  'M&S Select Whisky',        1, '2019-05-22', 1),
(3,  'Cashmere Crew Neck',       2, '2021-03-15', 1),
(4,  'Plant Kitchen Burger',     1, '2022-07-01', 1),
(5,  'Egyptian Cotton Bedset',   4, '2018-11-30', 1),
(6,  'Wireless Earbuds',         3, '2023-02-14', 1),
(7,  'Rose Gold Moisturiser',    5, '2020-09-09', 1),
(8,  'Classic Chino Trousers',   2, '2017-06-25', 0),
(9,  'Sparks Loyalty Card',      1, '2021-01-01', 1),
(10, 'Autograph Wool Coat',      2, '2022-10-03', 1);

INSERT INTO product_price_history (product_id, effective_date, price) VALUES
-- Per Una Midi Dress: due price points
(1,  '2020-01-10', 45.00),
(1,  '2023-06-01', 49.00),
-- M&S Select Whisky
(2,  '2019-05-22', 22.00),
(2,  '2024-01-01', 25.00),
-- Cashmere Crew Neck
(3,  '2021-03-15', 89.00),
(3,  '2024-03-01', 95.00),
-- Plant Kitchen Burger
(4,  '2022-07-01',  4.50),
-- Egyptian Cotton Bedset
(5,  '2018-11-30', 79.00),
(5,  '2022-09-01', 85.00),
-- Wireless Earbuds
(6,  '2023-02-14', 35.00),
-- Rose Gold Moisturiser
(7,  '2020-09-09', 18.00),
(7,  '2023-11-01', 20.00),
-- Classic Chino Trousers (discontinued)
(8,  '2017-06-25', 35.00),
-- Sparks Loyalty Card
(9,  '2021-01-01',  0.00),
-- Autograph Wool Coat
(10, '2022-10-03', 159.00),
(10, '2024-10-01', 175.00);

INSERT INTO store_product_transactions (product_id, store_id, transaction_date) VALUES
-- Manchester
(1,  1, '2024-01-15'),
(3,  1, '2024-02-20'),
(6,  1, '2024-03-05'),
(10, 1, '2024-04-18'),
(2,  1, '2024-05-30'),
-- London
(1,  2, '2024-01-20'),
(2,  2, '2024-02-14'),
(4,  2, '2024-03-22'),
(7,  2, '2024-04-09'),
(9,  2, '2024-06-01'),
-- Edinburgh
(3,  3, '2024-01-08'),
(5,  3, '2024-02-28'),
(8,  3, '2024-03-17'),
(10, 3, '2024-05-05'),
-- Cardiff
(2,  4, '2024-01-25'),
(4,  4, '2024-03-30'),
(6,  4, '2024-04-14'),
-- Belfast
(1,  5, '2024-02-10'),
(7,  5, '2024-03-25'),
(9,  5, '2024-05-15'),
-- Prodotti venduti in più negozi (utile per testare COUNT DISTINCT)
(1,  3, '2024-06-10'),  -- Per Una Dress anche a Edinburgh
(1,  4, '2024-06-15'),  -- Per Una Dress anche a Cardiff
(3,  2, '2024-07-01'),  -- Cashmere anche a London
(6,  2, '2024-07-20');  -- Earbuds anche a London