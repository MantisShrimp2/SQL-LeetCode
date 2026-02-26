# Last updated: 2/26/2026, 1:54:58 PM
1class Solution(object):
2    def merge(self, nums1, m, nums2, n):
3        """
4        :type nums1: List[int]
5        :type m: int
6        :type nums2: List[int]
7        :type n: int
8        :rtype: None Do not return anything, modify nums1 in-place instead.
9        """
10        for j in range(n):
11            nums1[m+j] = nums2[j]
12        nums1.sort()
13        