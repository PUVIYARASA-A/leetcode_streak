class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_value = max(nums)  # Find the maximum value in the nums list.
        n = len(nums)          # Get the length of the nums list.
        answer = 0             # Initialize the answer to 0.
        count_max = 0          # Initialize the count for the maximum value to 0.
        j = 0                  # Pointer to scan through the list.
      
        # Iterate over all elements in nums array.
        for i, x in enumerate(nums):
            # Move the j pointer and update count_max until we have counted k max_value or reached end of list.
            while j < n and count_max < k:
                count_max += nums[j] == max_value  # Increment count_max if nums[j] is max_value.
                j += 1                             # Increment j to move the window forward.
          
            # If we have counted k max_value, update the answer.
            if count_max < k:
                break  # If count_max is less than k, then break from the loop as further windows won't have k max_values.
            answer += n - j + 1  # Add the number of valid subarrays starting from i-th position.
          
            # Decrease count_max for the sliding window as we move past the i-th element.
            count_max -= x == max_value
      
        return answer  # Return the total number of valid subarrays.
