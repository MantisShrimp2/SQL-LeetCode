# Last updated: 2/26/2026, 5:50:12 PM
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        seen = {}
        k = 0

        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]] = True
                nums[k] = nums[i]
                k += 1

        return k
        