class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total_difference = 0  
        for i in range(1, n + 1):
            if i % m == 0:
                total_difference -= i
            else:
                total_difference += i
        return total_difference
