class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] 
        costs = [[float('inf')] * cols for _ in range(rows)]
        costs[0][0] = 0
        dq = deque([(0, 0, 0)]) 
        while dq:
            x, y, current_cost = dq.popleft()
            if current_cost > costs[x][y]:
                continue
            for i, (dx, dy) in enumerate(directions):
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    new_cost = current_cost if grid[x][y] == i + 1 else current_cost + 1
                    if new_cost < costs[nx][ny]:
                        costs[nx][ny] = new_cost
                        if new_cost == current_cost:
                            dq.appendleft((nx, ny, new_cost)) 
                        else:
                            dq.append((nx, ny, new_cost))
        return costs[rows - 1][cols - 1]
