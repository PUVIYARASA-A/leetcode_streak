class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if k == 0:
            return 0  # Edge case: No children to distribute to.

        left, right = 1, max(candies)
        best = 0
    
        while left <= right:
            mid = (left + right) // 2
            count = sum(c // mid for c in candies)  # Total children served
        
            if count >= k:
                best = mid  # Possible answer, try for more
                left = mid + 1
            else:
                right = mid - 1
    
        return best
