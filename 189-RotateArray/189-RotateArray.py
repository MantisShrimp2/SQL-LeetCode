# Last updated: 2/26/2026, 5:50:09 PM
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        k %= n 

        r = n - k

        new = nums[0:r]

        nums[0:r] = []

        nums.extend(new)
        