# Last updated: 2/27/2026, 4:27:35 PM
1class Solution(object):
2    def canJump(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: bool
6        """
7        m = 0 
8        for i ,n in enumerate(nums):
9 
10            if i > m: 
11                return False
12            m = max(m, i+n)
13
14        return True
15        