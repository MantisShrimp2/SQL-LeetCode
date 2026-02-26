# Last updated: 2/26/2026, 4:40:12 PM
1class Solution(object):
2    def rotate(self, nums, k):
3        """
4        :type nums: List[int]
5        :type k: int
6        :rtype: None Do not return anything, modify nums in-place instead.
7        """
8        n = len(nums)
9
10        k %= n 
11
12        r = n - k
13
14        new = nums[0:r]
15
16        nums[0:r] = []
17
18        nums.extend(new)
19        