class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
    
    # If total is odd, cannot partition equally
        if total % 2 != 0:
            return False

        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True  # Base case: zero sum is always possible

        for num in nums:
            # Traverse backwards to avoid overwriting
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[target]
