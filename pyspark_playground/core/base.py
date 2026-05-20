from loguru._logger import Logger
from pyspark.sql import SparkSession

from pyspark_playground.core.runtime import SparkRuntime


class SparkBase:

    def __init__(self, *, runtime: SparkRuntime | None = None) -> None:
        self.runtime = runtime or SparkRuntime()

    @property
    def spark(self) -> SparkSession:
        return self.runtime.spark

    @property
    def logger(self) -> Logger:
        return self.runtime.logger
