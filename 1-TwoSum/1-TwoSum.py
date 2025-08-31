# Last updated: 8/31/2025, 5:05:03 PM
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {} # Dictionary to store number and index 
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return[num_map[complement], i]
            num_map[num] = i












































































    



        -0
        