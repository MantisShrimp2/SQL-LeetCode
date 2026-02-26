# Last updated: 2/26/2026, 2:01:04 PM
1class Solution(object):
2    def removeElement(self, nums, val):
3        """
4        :type nums: List[int]
5        :type val: int
6        :rtype: int
7        """
8        k = 0
9        for n in nums:
10            if n != val:
11                nums[k] = n
12                k +=1
13        return k