class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        index_map = {num: i for i, num in enumerate(arr)}  # Store indices of elements
        dp = {}  # Stores the length of Fibonacci subsequence ending at (i, j)
        max_length = 0

        for j in range(len(arr)):
            for i in range(j):
                prev = arr[j] - arr[i]
                if prev in index_map and index_map[prev] < i:
                    k = index_map[prev]
                    dp[i, j] = dp.get((k, i), 2) + 1  # If exists, extend else start new
                    max_length = max(max_length, dp[i, j])

        return max_length if max_length >= 3 else 0
