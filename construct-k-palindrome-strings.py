from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # If k is greater than the length of the string, it's impossible
        if k > len(s):
            return False
        
        # Count character frequencies
        freq = Counter(s)
        
        # Count the number of characters with odd frequencies
        odd_count = sum(1 for count in freq.values() if count % 2 != 0)
        
        # Check if k is at least the number of odd frequencies
        return k >= odd_count
