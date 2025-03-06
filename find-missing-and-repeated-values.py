class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        nums = [num for row in grid for num in row]  # Flatten grid
        num_set = set()
        repeated = -1

        for num in nums:
            if num in num_set:
                repeated = num
            num_set.add(num)
        
        expected_sum = sum(range(1, n * n + 1))
        actual_sum = sum(nums)
        
        missing = expected_sum - (actual_sum - repeated)  # Fix missing value
        return [repeated, missing]
