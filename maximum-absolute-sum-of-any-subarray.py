class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = 0  # Maximum subarray sum
        min_sum = 0  # Minimum subarray sum
        curr_max = 0
        curr_min = 0

        for num in nums:
            curr_max = max(num, curr_max + num)  # Kadane's for max sum
            curr_min = min(num, curr_min + num)  # Kadane's for min sum
        
            max_sum = max(max_sum, curr_max)
            min_sum = min(min_sum, curr_min)

        return max(max_sum, abs(min_sum))  # Maximum absolute sum
