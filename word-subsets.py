class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        max_b_counter = Counter()
        for word in words2:
            max_b_counter |= Counter(word) 
        result = []
        for word in words1:
            if not max_b_counter - Counter(word):
                result.append(word)
        return result
