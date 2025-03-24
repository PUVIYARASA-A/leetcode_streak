class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        
        free_days = 0
        last_end = 0  # Track the last occupied day
        
        for start, end in meetings:
            # Count free days between meetings
            if start > last_end + 1:
                free_days += start - last_end - 1
            
            # Update last occupied day
            last_end = max(last_end, end)
        
        # Count free days after the last meeting
        if last_end < days:
            free_days += days - last_end
        
        return free_days
