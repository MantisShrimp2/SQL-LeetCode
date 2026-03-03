# Last updated: 3/3/2026, 10:07:37 AM
class Solution(object):
            
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        count = {}

        for num in set(nums1):
            count[num] = count.get(num,0) + 1
        for num in set(nums2):
            count[num] = count.get(num,0) + 1
        for num in set(nums3):
            count[num] = count.get(num,0) + 1
        
        return [num for num, freq in count.items() if freq >=2]
        
