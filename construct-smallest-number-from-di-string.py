class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []
        result = []
    
        for i in range(len(pattern) + 1):
            stack.append(str(i + 1))  # Push the next number
            if i == len(pattern) or pattern[i] == 'I':
                while stack:
                    result.append(stack.pop())  # Pop and append
        return "".join(result)
