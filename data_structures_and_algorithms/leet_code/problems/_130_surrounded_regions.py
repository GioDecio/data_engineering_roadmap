"""
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:
Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells 
and none of the region cells are on the edge of the board.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. 
You do not need to return anything.
"""


def sourrounded_regions(board):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    # print("\n")

    if len(board) != 1:

        def is_border(i, j):
            if i == 0 or j == 0 or i == len(board) - 1 or j == len(board[0]) - 1:
                return True
            return False

        def traverse(i, j):
            board[i][j] = "NS"
            if i - 1 >= 0 and board[i - 1][j] == "O":
                traverse(i - 1, j)  # Check up
            if j - 1 >= 0 and board[i][j - 1] == "O":
                traverse(i, j - 1)  # Check left
            if i + 1 < len(board) and board[i + 1][j] == "O":
                traverse(i + 1, j)  # check down
            if j + 1 < len(board[0]) and board[i][j + 1] == "O":
                traverse(i, j + 1)  # Check right

        # Scan the board
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "O" and is_border(i, j):
                    traverse(i, j)

        # Second loop: convert remaining 'O's to 'X's
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "NS":
                    board[i][j] = "O"

    return board


board1 = [["X", "X"], ["O", "O"]]
board2 = [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]
board3 = [["O", "O", "X"], ["O", "X", "O"], ["X", "X", "X"]]
board4 = [["X", "X", "X"], ["X", "O", "X"], ["X", "X", "X"]]
board5 = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"],
]
board6 = [["X"]]
board7 = [["O"]]
board8 = [
    ["O", "X", "X", "O", "X"],
    ["X", "X", "X", "X", "O"],
    ["X", "X", "O", "X", "X"],
    ["O", "X", "X", "X", "O"],
    ["X", "X", "O", "X", "O"],
]

[
    ["O", "X", "X", "O", "X"],
    ["X", "X", "X", "X", "O"],
    ["X", "X", "X", "X", "X"],
    ["O", "X", "X", "X", "O"],
    ["X", "X", "O", "X", "O"],
]

print(sourrounded_regions(board1))
print(sourrounded_regions(board2))
print(sourrounded_regions(board3))
print(sourrounded_regions(board4))
print(sourrounded_regions(board5))
print(sourrounded_regions(board6))
print(sourrounded_regions(board7))
print(f"{sourrounded_regions(board8)}")


[
    ["O", "X", "X", "O", "X"],
    ["X", "O", "O", "X", "O"],
    ["X", "O", "X", "O", "X"],
    ["O", "X", "O", "O", "O"],
    ["X", "X", "O", "X", "O"],
]

[
    ["O", "X", "X", "O", "X"],
    ["X", "X", "X", "X", "O"],
    ["X", "X", "X", "X", "X"],
    ["O", "X", "X", "X", "O"],
    ["X", "X", "O", "X", "O"],
]
