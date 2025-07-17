class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)]

    # Extend the pattern xyxyxy...xy.
        for x in nums:
            for y in range(k):
                dp[x % k][y] = dp[y][x % k] + 1

        return max(map(max, dp))
