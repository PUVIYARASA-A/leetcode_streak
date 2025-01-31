class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        island_sizes = {}  # Stores island sizes by index
        index = 2  # Start marking islands from 2 to differentiate from 1s

        def dfs(r: int, c: int, index: int) -> int:
            """Perform DFS to find island size and mark cells with index."""
            stack = [(r, c)]
            grid[r][c] = index
            size = 0

            while stack:
                x, y = stack.pop()
                size += 1
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = index
                        stack.append((nx, ny))

            return size

        # Step 1: Identify all islands and store their sizes
        max_size = 0
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    island_sizes[index] = dfs(r, c, index)
                    max_size = max(max_size, island_sizes[index])
                    index += 1

        # Step 2: Try flipping each 0 and calculate the potential max island
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen = set()
                    for dx, dy in directions:
                        nr, nc = r + dx, c + dy
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                            seen.add(grid[nr][nc])

                    new_size = 1 + sum(island_sizes[i] for i in seen)
                    max_size = max(max_size, new_size)

        return max_size
