# Last updated: 3/3/2026, 9:27:08 AM
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        return sum( i < j for i,j in enumerate(sorted(citations, reverse=True)))

        