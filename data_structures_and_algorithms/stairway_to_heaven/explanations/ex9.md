```markdown
# Pandas DataFrame Row-to-Column Transformation Exercises

## Exercise 1: Extract Single Value as New Column

### Task

Given a DataFrame with two rows, extract a specific value from one row and add it as a new column to the remaining row.

### Input

```
| index | A | B | C |
|-------|---|---|---|
| 1     | 1 | 2 | 3 |
| 2     | 4 | 5 | 6 |
```

### Output

```
| index | A | B | C | new_col |
|-------|---|---|---|---------|
| 1     | 1 | 2 | 3 | 5       |
```

The value at row 2, column B becomes a new column in row 1.

### Constraints

- Do not use hardcoded index positions or magic numbers
- Use regex patterns to identify rows and columns dynamically
- Handle edge cases: what if the pattern matches zero or multiple indices?

### Hints

1. Consider writing a helper function to find indices by regex pattern
2. Think carefully about whether you need `.copy()` when slicing DataFrames
3. `pd.Index` objects are iterable and can be filtered with list comprehensions

---

## Exercise 2: Expand Entire Row as New Columns

### Task

Given a DataFrame with two rows, transform all values from one row into new columns of the remaining row, using a suffix to indicate the source.

### Input

```
| index | A | B | C |
|-------|---|---|---|
| 1     | 1 | 2 | 3 |
| 2     | 4 | 5 | 6 |
```
### Output
```
| index | A | B | C | A_from_row2 | B_from_row2 | C_from_row2 |
|-------|---|---|---|-------------|-------------|-------------|
| 1     | 1 | 2 | 3 | 4           | 5           | 6           |
```
Each value from row 2 becomes a new column with suffix `_from_row2`.

### Constraints

- Do not use hardcoded index positions or magic numbers
- Use regex patterns to identify the source row dynamically
- The suffix should be generated from the source row's index name

### Hints

1. Iterate over the original columns to create new column names
2. Consider using f-strings for dynamic column naming
3. The source row can be accessed as a Series and iterated
```