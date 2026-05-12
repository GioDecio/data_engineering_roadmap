def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        for j in range(len(matrix[i]) // 2):
            matrix[i][j], matrix[i][len(matrix[i]) - 1 - j] = (
                matrix[i][len(matrix[i]) - 1 - j],
                matrix[i][j],
            )


test_cases = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
]
expected_outputs = [
    [[7, 4, 1], [8, 5, 2], [9, 6, 3]],
    [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]],
]

for test_case in test_cases:

    matrix = rotate(test_case)
    print(matrix)
