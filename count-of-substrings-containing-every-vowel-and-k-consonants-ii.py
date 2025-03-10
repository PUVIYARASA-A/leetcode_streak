class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        VOWELS = 'aeiou'

        def substringsWithAtMost(k: int) -> int:
            if k < 0:
                return 0

            res = 0
            vowels = 0
            uniqueVowels = 0
            vowelLastSeen = {}

            l = 0
            for r, c in enumerate(word):
                if c in VOWELS:
                    vowels += 1
                    if c not in vowelLastSeen or vowelLastSeen[c] < l:
                        uniqueVowels += 1
                    vowelLastSeen[c] = r

                while (r - l + 1 - vowels) > k:
                    if word[l] in VOWELS:
                        vowels -= 1
                        if vowelLastSeen[word[l]] == l:
                            uniqueVowels -= 1
                    l += 1

                if uniqueVowels == 5:
                    if all(v in vowelLastSeen for v in VOWELS):
                        res += min(vowelLastSeen[vowel] for vowel in VOWELS) - l + 1

            return res

        return substringsWithAtMost(k) - substringsWithAtMost(k - 1)
