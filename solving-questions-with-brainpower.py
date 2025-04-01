class Solution:
    def __init__(self):
        self.memo = {}
    
    def mostPoints(self, questions: List[List[int]]) -> int:
        return self.dp(0, questions)

    def dp(self, i: int, questions: List[List[int]]) -> int:
        if i >= len(questions):
            return 0  # Base case: No more questions left to process
        
        if i in self.memo:
            return self.memo[i]  # Return already computed result

        points, skip = questions[i]
        take = points + self.dp(i + skip + 1, questions)

        skip_question = self.dp(i + 1, questions)

        self.memo[i] = max(take, skip_question)
        return self.memo[i]
