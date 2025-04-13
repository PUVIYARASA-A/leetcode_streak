class Solution:
    def countGoodNumbers(self, n: int) -> int:
        M = 10 ** 9 + 7
        
        def power(base, exp):
            if exp == 0: return 1
            
            v = power(base, exp // 2)
            
            if exp % 2 == 0:
                return (v * v) % M
            else:
                return (v * v * base) % M
        
        even = int(n // 2 + int(n % 2 != 0))
        odd = int(n // 2)
         
        e = power(5, even)
        o = power(4, odd)
        
        return (e * o) % M

     
