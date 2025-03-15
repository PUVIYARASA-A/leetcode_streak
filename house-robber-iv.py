class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def canRob(mid):
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= mid:  # If house is robbable under mid threshold
                    count += 1
                    i += 1  # Skip next house to prevent adjacent robbery
                i += 1
            return count >= k

        left, right = min(nums), max(nums)  # Search between the min and max house values
        while left < right:
            mid = (left + right) // 2
            if canRob(mid):
                right = mid  # Try a smaller max amount
            else:
                left = mid + 1  # Increase the threshold
        return left
