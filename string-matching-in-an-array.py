class Solution:
    def precomputeLPS(self, words):
        lps = []
        for word in words:
            m = len(word)
            wordLPS = [0] * m
            i = 1
            j = 0
            while i < m:
                if word[i] == word[j]:
                    wordLPS[i] = j + 1
                    i += 1
                    j += 1
                elif j > 0:
                    j = wordLPS[j - 1]
                else:
                    i += 1
            lps.append(wordLPS)
        return lps

    def stringMatcher(self, pattern, patternLPS, text):
        patternSize = len(pattern)
        textSize = len(text)
        i = 0
        j = 0
        while i < patternSize and j < textSize:
            if pattern[i] == text[j]:
                i += 1
                j += 1
            if i == patternSize:
                return True
            if j < textSize and pattern[i] != text[j]:
                if i > 0:
                    i = patternLPS[i - 1]
                else:
                    j += 1
        return False

    def stringMatching(self, words):
        n = len(words)
        words.sort(key=len)  # Sort words by length
        lps = self.precomputeLPS(words)
        res = []
        for i in range(n - 1):
            for j in range(i + 1, n):
                if self.stringMatcher(words[i], lps[i], words[j]):
                    res.append(words[i])
                    break
        return res
