# Data Engineering Roadmap

Learning repo covering data structures & algorithms and PySpark.

## Structure

```
data_structures_and_algorithms/   # leet_code, stairway_to_heaven, book, practice
pyspark_playground/                          # PySpark exercises and datasets
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

## Docker

```bash
docker build -t data-engineering-roadmap .

# run a PySpark script
docker run --rm data-engineering-roadmap python3 pyspark_playground/1_e_load_and_transform_data.py

# run tests
docker run --rm data-engineering-roadmap uv run pytest tests/

# interactive shell
docker run --rm -it data-engineering-roadmap bash
```
