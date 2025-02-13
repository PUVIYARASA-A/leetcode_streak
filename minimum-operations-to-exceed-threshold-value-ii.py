class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        operations = 0

        while len(nums) > 1 and nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            new_element = min(x, y) * 2 + max(x, y)
            heapq.heappush(nums, new_element)
            operations += 1

        if nums[0] >= k:
            return operations
        else:
            return -1  # Indicates it's not possible to achieve the condition
