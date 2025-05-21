class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        nrows, ncols = len(matrix), len(matrix[0])
        first_row_has_zero = any(value == 0 for value in matrix[0])
        first_col_has_zero = any(matrix[row][0] == 0 for row in range(nrows))

        for row in range(1, nrows):
            for col in range(1, ncols):
                if matrix[row][col] == 0:
                    matrix[row][0] = matrix[0][col] = 0

        for row in range(1, nrows):
            for col in range(1, ncols):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        if first_row_has_zero:
            for col in range(ncols):
                matrix[0][col] = 0

        if first_col_has_zero:
            for row in range(nrows):
                matrix[row][0] = 0
