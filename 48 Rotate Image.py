class Solution:
    def rotate(self, matrix):
        n = len(matrix)

        # Transpose
        for r in range(n):
            for c in range(r + 1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        # Reverse rows
        for r in range(n):
            matrix[r].reverse()
        