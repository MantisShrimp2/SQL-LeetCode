# Last updated: 2/27/2026, 3:58:47 PM
1class Solution(object):
2    def removeDuplicates(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7
8        count =0
9        current = 1
10        for i in range(1, len(nums)):
11            if nums[i] != nums[i-1]:
12                count = 0
13                nums[current] = nums[i]
14                current +=1
15            else:
16                count +=1
17                if count <=1:
18                    nums[current] = nums[i]
19                    current +=1
20        return current