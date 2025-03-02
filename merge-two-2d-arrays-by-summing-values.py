class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        merged_dict = {}

        for key, value in nums1 + nums2:  # Merge both arrays
            merged_dict[key] = merged_dict.get(key, 0) + value

        return sorted(merged_dict.items())
