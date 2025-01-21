class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        top_prefix_sum = [0] * n
        bottom_prefix_sum = [0] * n
        top_prefix_sum[0] = grid[0][0]
        bottom_prefix_sum[0] = grid[1][0]
        for i in range(1, n):
            top_prefix_sum[i] = top_prefix_sum[i - 1] + grid[0][i]
            bottom_prefix_sum[i] = bottom_prefix_sum[i - 1] + grid[1][i]
        result = float('inf')
        for i in range(n):
            top_remaining = top_prefix_sum[-1] - top_prefix_sum[i]  # Remaining on top row
            bottom_remaining = bottom_prefix_sum[i - 1] if i > 0 else 0
            second_robot_score = max(top_remaining, bottom_remaining)
            result = min(result, second_robot_score)
        return result
