class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = {'a': 0, 'b': 0, 'c': 0}  # Frequency of a, b, c
        left = 0  # Left boundary of the window
        result = 0  # Count of valid substrings
        for right in range(len(s)):
            count[s[right]] += 1  # Expand window by including s[right]
            while all(count[ch] > 0 for ch in "abc"):
                result += len(s) - right  # Count substrings ending beyond `right`
                count[s[left]] -= 1  # Shrink window
                left += 1  # Move left pointer to minimize the window
        return result
