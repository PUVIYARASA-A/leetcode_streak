class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = current_sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:  # Continue ascending subarray
                current_sum += nums[i]
            else:  # Start a new subarray
                current_sum = nums[i]
            
            max_sum = max(max_sum, current_sum)

        return max_sum
