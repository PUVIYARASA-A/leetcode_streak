from collections import defaultdict
from heapq import heappush, heappop
from math import inf

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # Create a default dictionary to hold events keyed by start date
        event_dict = defaultdict(list)
      
        # Initialize variables to track the earliest and latest event dates
        earliest_start, latest_end = inf, 0
      
        # Populate event_dict with events and update earliest_start and latest_end
        for start, end in events:
            event_dict[start].append(end)
            earliest_start = min(earliest_start, start)
            latest_end = max(latest_end, end)
      
        # Initialize an empty min-heap to store active events' end dates
        min_heap = []
      
        # Counter for the maximum number of events one can attend
        max_events_attended = 0
      
        # Iterate over each day within the range of event dates
        for day in range(earliest_start, latest_end + 1):
            # Remove events that have already ended
            while min_heap and min_heap[0] < day:
                heappop(min_heap)
          
            # Push all end dates of events starting today onto the heap
            for end in event_dict[day]:
                heappush(min_heap, end)
          
            # If there are any events available to attend today, attend one and increment count
            if min_heap:
                max_events_attended += 1
                heappop(min_heap)  # Remove the event that was attended
      
        # Return the total number of events attended
        return max_events_attended
