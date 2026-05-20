# Data Engineering Roadmap

Learning repo covering data structures & algorithms and PySpark.

## Structure

```
data_structures_and_algorithms/   # leet_code, stairway_to_heaven, book, practice
pyspark_playground/               # PySpark exercises and datasets
sql_lab/
└── pgsql_lab/                    # PostgreSQL playground (Docker + psycopg2)
tests/                            # pytest suite for DSA section
```

## Setup

```bash
uv sync                          # DSA environment (pytest, loguru)
```

## PySpark (local)

PySpark requires Python 3.11 — the repo is pinned to it via `.python-version`.

```bash
uv venv --python 3.11            # create venv with Python 3.11 (first time only)
uv sync --group pyspark          # install PySpark alongside default dependencies
uv run python3 pyspark_playground/<script>.py
```

## Running tests

```bash
uv run pytest tests/
```

## Docker — PySpark

```bash
docker build -f Dockerfile.pyspark -t data-engineering-roadmap .

# run a PySpark script
docker run --rm data-engineering-roadmap python3 pyspark_playground/1_e_load_and_transform_data.py

# run tests
docker run --rm data-engineering-roadmap uv run pytest tests/

# interactive shell
docker run --rm -it data-engineering-roadmap bash
```

## SQL Lab — PostgreSQL

```bash
cd sql_lab/pgsql_lab
docker compose up --build        # start Postgres + Python app
docker compose up db             # start only the database
```

Connect with any Postgres client:

| Parameter | Value |
|---|---|
| Host | `localhost` |
| Port | `5432` |
| User | `lab_user` |
| Password | `lab_password` |
| Database | `lab_db` |

See `sql_lab/pgsql_lab/README.md` for full details.
