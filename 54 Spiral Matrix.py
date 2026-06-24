class Solution:
    def spiralOrder(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bottom = rows - 1
        left = 0
        right = cols - 1

        ans = []

        while top <= bottom and left <= right:

            # Left -> Right
            for c in range(left, right + 1):
                ans.append(matrix[top][c])
            top += 1

            # Top -> Bottom
            for r in range(top, bottom + 1):
                ans.append(matrix[r][right])
            right -= 1

            # Right -> Left
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    ans.append(matrix[bottom][c])
                bottom -= 1

            # Bottom -> Top
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    ans.append(matrix[r][left])
                left += 1

        return ans