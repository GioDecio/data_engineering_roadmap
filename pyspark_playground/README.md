# PySpark Playground

## Architecture

Exercises follow a dependency injection pattern.

### `core/runtime.py` — `SparkRuntime`

Creates and manages `SparkSession` and `logger`. One instance per process (class-level singleton).

- `SparkSession` is lazy: created only when first accessed
- Checks for an active session first (`getActiveSession`)
- Logger via `loguru`

### `core/base.py` — `SparkBase`

Base class that receives a `SparkRuntime` and exposes `self.spark` and `self.logger` as properties.

### Pattern in exercises

```python
class ExN(SparkBase):
    def __init__(self, runtime: SparkRuntime, df):
        super().__init__(runtime=runtime)
        self.df = df

if __name__ == "__main__":
    runtime = SparkRuntime()
    df = runtime.spark.createDataFrame(data, columns)
    ex = ExN(runtime, df)
```

`SparkSession` is never instantiated directly in exercise classes — it is injected via `SparkRuntime`.
