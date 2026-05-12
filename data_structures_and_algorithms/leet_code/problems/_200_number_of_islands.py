"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""


def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """

    def traverse(grid, i, j):

        # base case
        grid[i][j] = "0"  # mark cell as visited

        # Scan adjacent cells
        if j + 1 < len(grid[i]) and grid[i][j + 1] == "1":  # check right
            traverse(grid, i, j + 1)
        if i + 1 < len(grid) and grid[i + 1][j] == "1":  # check down
            traverse(grid, i + 1, j)
        if i - 1 >= 0 and grid[i - 1][j] == "1":  # check up
            traverse(grid, i - 1, j)
        if j - 1 < len(grid[i]) and j - 1 >= 0 and grid[i][j - 1] == "1":  # check left
            traverse(grid, i, j - 1)

    n_islands = 0
    for i in range(len(grid)):
        print(f"Exploring row: {i+1}")
        for j in range(len(grid[i])):
            if grid[i][j] == "1":
                traverse(grid, i, j)
                n_islands += 1
    print("\n")

    return n_islands


grid1 = [["1", "1"], ["1", "1"], ["1", "1"], ["0", "0"]]
grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
grid3 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]
grid4 = [["0", "0"], ["0", "0"], ["0", "0"], ["0", "0"]]

grids = [grid1, grid2, grid3, grid4]
outputs = [1, 3, 1, 0]
keys = [1, 2, 3, 4]
out_d = dict(zip(keys, outputs))

for idx, grid in enumerate(grids):
    print(
        f"Expected output for grid{idx+1}: {out_d[idx+1]}: current: {numIslands(grid)}___--------"
    )
