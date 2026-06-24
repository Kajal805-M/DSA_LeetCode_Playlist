class Solution:
    def setZeroes(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        row0 = False
        col0 = False

        # Check if first row has any zero
        for c in range(cols):
            if matrix[0][c] == 0:
                row0 = True
                break

        # Check if first column has any zero
        for r in range(rows):
            if matrix[r][0] == 0:
                col0 = True
                break

        # Mark rows and columns
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        # Set elements to zero based on markers
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # Set first row to zero
        if row0:
            for c in range(cols):
                matrix[0][c] = 0

        # Set first column to zero
        if col0:
            for r in range(rows):
                matrix[r][0] = 0