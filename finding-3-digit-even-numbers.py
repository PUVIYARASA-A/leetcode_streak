class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ans = []
        count = collections.Counter(digits)

        for a in range(1, 10):
            if count[a] > 0:  # First digit must be nonzero
                for b in range(0, 10):
                    if count[b] > (b == a):
                        for c in range(0, 10, 2):  # Last digit must be even
                            if count[c] > (c == a) + (c == b):
                                ans.append(a * 100 + b * 10 + c)

        return sorted(ans)
