class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_num = 0
        max_diff = 0
        max_value = 0

        for num in nums:
            max_value = max(max_value, max_diff * num)
            max_num = max(max_num, num)
            max_diff = max(max_diff, max_num - num)

        return max_value
