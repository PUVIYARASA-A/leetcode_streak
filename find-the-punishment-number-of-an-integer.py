class Solution:
    def punishmentNumber(self, n: int) -> int:
        def is_valid(num_str, target, index, current_sum):
            """Recursive function to check if num_str can be split into parts summing to target."""
            if index == len(num_str):
                return current_sum == target

            for j in range(index, len(num_str)):
                part = int(num_str[index:j + 1])
                if is_valid(num_str, target, j + 1, current_sum + part):
                    return True

            return False

        total = 0
        for i in range(1, n + 1):
            square_str = str(i * i)
            if is_valid(square_str, i, 0, 0):
                total += i * i

        return total
