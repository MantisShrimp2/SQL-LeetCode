# Last updated: 2/26/2026, 2:11:41 PM
1class Solution(object):
2    def removeDuplicates(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        
8        seen = {}
9        k = 0
10
11        for i in range(len(nums)):
12            if nums[i] not in seen:
13                seen[nums[i]] = True
14                nums[k] = nums[i]
15                k += 1
16
17        return k
18        