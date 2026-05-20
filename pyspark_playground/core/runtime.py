from loguru import logger as _root_logger
from loguru._logger import Logger
from pyspark.sql import SparkSession


class SparkRuntime:
    """Dependency-injection container. One instance per process."""

    _SPARK: SparkSession | None = None

    def __init__(self, *, app_name: str = "pyspark_playground") -> None:
        self.app_name = app_name
        self._spark: SparkSession | None = None
        self._logger: Logger | None = None

    @property
    def spark(self) -> SparkSession:
        if self._spark is not None:
            return self._spark
        if SparkRuntime._SPARK is not None:
            self._spark = SparkRuntime._SPARK
            return self._spark
        active = SparkSession.getActiveSession()
        if active is not None:
            SparkRuntime._SPARK = active
            self._spark = active
            return self._spark
        SparkRuntime._SPARK = SparkSession.builder.appName(self.app_name).getOrCreate()
        self._spark = SparkRuntime._SPARK
        return self._spark

    @property
    def logger(self) -> Logger:
        if self._logger is None:
            self._logger = _root_logger.bind(app_name=self.app_name)
        return self._logger
