class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        # Extract horizontal and vertical intervals from rectangles
        horizontal_intervals = [(x1, x2) for x1, _, x2, _ in rectangles]
        vertical_intervals = [(y1, y2) for _, y1, _, y2 in rectangles]
        
        # Check if the maximum count of merged intervals in either direction is at least 3
        return max(self._count_merged_intervals(horizontal_intervals),
                   self._count_merged_intervals(vertical_intervals)) >= 3

    def _count_merged_intervals(self, intervals: List[tuple]) -> int:
        # Sort intervals based on the start coordinate
        intervals.sort()
        count = 0
        prev_end = 0

        for start, end in intervals:
            if start < prev_end:
                # Merge overlapping intervals by updating the end coordinate
                prev_end = max(prev_end, end)
            else:
                # Non-overlapping interval found, increment count
                prev_end = end
                count += 1

        return count
