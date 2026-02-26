# Last updated: 2/26/2026, 4:20:12 PM
1class Solution(object):
2    def majorityElement(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7
8        maj_dict = {}
9
10        for n in nums:
11            if n not in maj_dict:
12                maj_dict[n] =1
13            else:
14                maj_dict[n] +=1
15        max_key = max(maj_dict, key=maj_dict.get)
16        return max_key
17        