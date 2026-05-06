class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if len(board) != 1:

            def traverse(board, i, j):
                board[i][j] = "NS"  # mark visited cell as non surroundable
                if i == 0 and board[i + 1][j] == "O":  # Check down
                    traverse(board, i + 1, j)
                if i == len(board) - 1 and board[i - 1][j] == "O":  # Check up
                    traverse(board, i - 1, j)
                if j == 0 and board[i][j + 1] == "O":  # Check right
                    traverse(board, i, j + 1)
                if j == len(board[i]) - 1 and board[i][j - 1] == "O":  # Check left
                    traverse(board, i, j - 1)

            def is_border(board, i, j):
                if i == 0:
                    return True
                if j == 0:
                    return True
                if i == len(board) - 1:
                    return True
                if j == len(board[i]) - 1:
                    return True
                return False

            # Scan the board
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if is_border(board, i, j) and board[i][j] == "O":
                        traverse(board, i, j)
            # Mark non surroundable with "O"
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == "NS":
                        board[i][j] = "O"
                    else:
                        board[i][j] = "X"

        return board
