class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def canTransform(k):
            d = [0] * (len(nums) + 1)
            for l, r, val in queries[:k]:
                d[l] += val
                if r + 1 < len(d):
                    d[r + 1] -= val
            current_decrement = 0
            for i in range(len(nums)):
                current_decrement += d[i]
                if nums[i] > current_decrement:
                    return False
            return True

        left, right = 0, len(queries)
        while left < right:
            mid = (left + right) // 2
            if canTransform(mid):
                right = mid
            else:
                left = mid + 1

        return left if canTransform(left) else -1
