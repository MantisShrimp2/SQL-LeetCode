# Last updated: 2/25/2026, 3:18:19 PM
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        new_list = sorted(nums1 + nums2)
        length = len(new_list)
        mid_index = length // 2


        if length % 2 == 0:  # even length
            left = new_list[mid_index - 1]
            right = new_list[mid_index]
            return (left + right) / 2.0
        else:  # odd length
            return float(new_list[mid_index])


