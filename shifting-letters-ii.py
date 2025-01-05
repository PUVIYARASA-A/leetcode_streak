class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)  # Difference Array to record overall changes

        # Mark changes
        for shift in shifts:
            if shift[2] == 1:
                diff[shift[0]] += 1
                diff[shift[1] + 1] -= 1
            else:
                diff[shift[0]] -= 1
                diff[shift[1] + 1] += 1

        # Get actual updated values from difference array
        for i in range(1, n + 1):
            diff[i] += diff[i - 1]

        # Build new string
        res = []
        for i in range(n):
            count = diff[i] % 26
            if count < 0:
                count += 26

            curr = chr((ord(s[i]) - ord('a') + count) % 26 + ord('a'))
            res.append(curr)

        return ''.join(res)
