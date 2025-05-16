from typing import List

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        
        def hamming_distance(w1: str, w2: str) -> int:
            return sum(c1 != c2 for c1, c2 in zip(w1, w2))

        dp = [1] * n
        prev = [-1] * n

        for i in range(n):
            for j in range(i):
                if groups[i] != groups[j] and len(words[i]) == len(words[j]):
                    if hamming_distance(words[i], words[j]) == 1:
                        if dp[j] + 1 > dp[i]:
                            dp[i] = dp[j] + 1
                            prev[i] = j

        # Find the index with the maximum DP value
        max_index = max(range(n), key=lambda i: dp[i])

        # Reconstruct the longest valid subsequence
        result = []
        while max_index != -1:
            result.append(words[max_index])
            max_index = prev[max_index]

        return result[::-1]
