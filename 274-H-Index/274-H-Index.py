# Last updated: 3/1/2026, 1:58:22 PM
1class Solution(object):
2    def hIndex(self, citations):
3        """
4        :type citations: List[int]
5        :rtype: int
6        """
7        return sum( i < j for i,j in enumerate(sorted(citations, reverse=True)))
8
9        