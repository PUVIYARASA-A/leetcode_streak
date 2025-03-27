class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # Step 1: Find the dominant element of the entire array
        count = Counter(nums)
        n = len(nums)
        
        # Dominant element is the one that appears more than n/2 times
        dominant = None
        for key, val in count.items():
            if val > n // 2:
                dominant = key
                break

        if dominant is None:
            return -1  # No valid split possible
        
        # Step 2: Traverse the array to find the minimum valid split index
        left_count = 0  # Count of dominant element in left partition
        total_count = count[dominant]

        for i in range(n - 1):  # Stop at n-1 because at least 1 element should be in right part
            if nums[i] == dominant:
                left_count += 1

            left_size = i + 1
            right_size = n - left_size
            right_count = total_count - left_count

            if left_count * 2 > left_size and right_count * 2 > right_size:
                return i  # Found valid split index

        return -1  # No valid split found
