class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged_array = nums1 + nums2
        merged_array.sort()
        length = len(merged_array)
        median = 0

        if length % 2 == 0:
            median = (merged_array[int(length/2)] + merged_array[int(length/2) - 1]) / 2
        else:
            median = merged_array[int(length/2)]

        return median
