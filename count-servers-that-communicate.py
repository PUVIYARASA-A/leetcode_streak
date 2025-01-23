class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        row_count = [0] * rows
        col_count = [0] * cols
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1
        total_servers = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    if row_count[i] > 1 or col_count[j] > 1:
                        total_servers += 1
        return total_servers
