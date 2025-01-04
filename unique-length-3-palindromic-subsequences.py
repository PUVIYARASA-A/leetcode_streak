class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        
        # STEP-1: Get first & last occurrences of each char
        first_last = {}
        for i, c in enumerate(s):
            if c not in first_last:
                first_last[c] = [i, i]
            else:
                first_last[c][1] = i
        
        # STEP-2: Find unique elements count in range
        count = 0
        for _, (first, last) in first_last.items():
            if first == last:
                continue
            count += len(set(s[first + 1:last]))
        
        return count
