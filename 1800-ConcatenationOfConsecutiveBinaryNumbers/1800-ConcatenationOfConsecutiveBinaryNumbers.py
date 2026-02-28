# Last updated: 2/28/2026, 6:04:24 PM
class Solution(object):
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """

        mod = 10**9 + 7
        ans = 0

        for i in range(1,n+1):
            ans = ((ans << i.bit_length()) + i) % mod
        return ans
        