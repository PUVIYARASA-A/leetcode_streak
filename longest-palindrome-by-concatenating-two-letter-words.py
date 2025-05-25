class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        word_count = Counter(words)
        length_of_palindrome = central_letter_pair_count = 0
      
        # Counter.items() contains pairs of (word, count)
        for word, count in word_count.items():
            # Check if the word is a pair of identical letters, like "aa"
            if word[0] == word[1]:
                # Count of such word pairs that can be used as the central part of the palindrome
                central_letter_pair_count += count % 2
                # Add the count (rounded down to the nearest even number) times 2 to the length
                length_of_palindrome += (count // 2) * 4
            else:
                # For other pairs, add the minimum count of the pair and its reverse pair to the length
                length_of_palindrome += min(count, word_count[word[::-1]]) * 2
      
        # If there are pairs of identical letters, we could place exactly one in the center of the palindrome
        length_of_palindrome += 2 if central_letter_pair_count else 0
      
        return length_of_palindrome
