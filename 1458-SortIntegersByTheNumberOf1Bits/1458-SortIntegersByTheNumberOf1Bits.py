# Last updated: 2/25/2026, 3:18:16 PM
class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        return sorted(arr,key=lambda x: (bin(x).count('1'), x))
        