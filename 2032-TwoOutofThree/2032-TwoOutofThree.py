# Last updated: 3/3/2026, 10:06:54 AM
1class Solution(object):
2            
3    def twoOutOfThree(self, nums1, nums2, nums3):
4        """
5        :type nums1: List[int]
6        :type nums2: List[int]
7        :type nums3: List[int]
8        :rtype: List[int]
9        """
10        count = {}
11
12        for num in set(nums1):
13            count[num] = count.get(num,0) + 1
14        for num in set(nums2):
15            count[num] = count.get(num,0) + 1
16        for num in set(nums3):
17            count[num] = count.get(num,0) + 1
18        
19        return [num for num, freq in count.items() if freq >=2]
20        
21