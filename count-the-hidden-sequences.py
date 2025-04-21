class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        min_val = max_val = current = 0
    
        for diff in differences:
            current += diff
            min_val = min(min_val, current)
            max_val = max(max_val, current)
    
        # Calculate the range of possible starting values
        start_min = lower - min_val
        start_max = upper - max_val
    
        # The number of valid starting values
        return max(0, start_max - start_min + 1)
