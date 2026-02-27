# Last updated: 2/27/2026, 9:06:30 PM
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m = 0 
        for i ,n in enumerate(nums):
 
            if i > m: 
                return False
            m = max(m, i+n)

        return True
        