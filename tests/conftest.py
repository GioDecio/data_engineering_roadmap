import pytest
from pyspark.sql import SparkSession
from pyspark_playground.core.runtime import SparkRuntime


@pytest.fixture(scope="session")
def spark():
    session = (
        SparkSession.builder.master("local")
        .appName("test")
        .config("spark.ui.enabled", "false")
        .getOrCreate()
    )
    yield session
    session.stop()


@pytest.fixture(scope="session")
def runtime(spark):
    rt = SparkRuntime()
    rt._spark = spark
    return rt
