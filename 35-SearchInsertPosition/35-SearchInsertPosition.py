# Last updated: 3/6/2026, 8:58:58 AM
1class Solution(object):
2    def searchInsert(self, nums, target):
3        """
4        :type nums: List[int]
5        :type target: int
6        :rtype: int
7        """
8        #do a binary search
9        l, r = 0, len(nums) - 1
10
11        while l <=r:
12            #search from the middle
13            mid = (l+r) //2
14            if nums[mid] < target:
15                l = mid+1
16            elif nums[mid] == target and nums[mid-1] !=target:
17                return mid
18            else:
19                r = mid -1
20        return l
21