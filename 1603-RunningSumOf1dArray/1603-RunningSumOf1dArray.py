# Last updated: 2/26/2026, 11:32:10 AM
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        return nums
        