from pyspark.sql import DataFrame


def show(df: DataFrame) -> None:
    try:
        display(df)
    except NameError:
        df.show()
