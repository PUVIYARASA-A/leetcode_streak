class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        num_positions = {}
        rows, cols = len(mat), len(mat[0])
        for r in range(rows):
            for c in range(cols):
                num_positions[mat[r][c]] = (r, c)
        row_count = defaultdict(int)
        col_count = defaultdict(int)
        for i, num in enumerate(arr):
            if num in num_positions:
                r, c = num_positions[num]
                row_count[r] += 1
                col_count[c] += 1
                if row_count[r] == cols or col_count[c] == rows:
                    return i
        return -1
