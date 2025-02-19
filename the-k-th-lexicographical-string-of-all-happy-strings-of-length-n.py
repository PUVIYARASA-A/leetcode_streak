class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        happy_strings = ["".join(s) for s in product("abc", repeat=n) if all(s[i] != s[i+1] for i in range(n-1))]
        return happy_strings[k-1] if k <= len(happy_strings) else ""
