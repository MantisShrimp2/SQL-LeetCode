# Last updated: 2/28/2026, 11:01:16 AM
1class Solution(object):
2    def concatenatedBinary(self, n):
3        """
4        :type n: int
5        :rtype: int
6        """
7
8        mod = 10**9 + 7
9        ans = 0
10
11        for i in range(1,n+1):
12            ans = ((ans << i.bit_length()) + i) % mod
13        return ans
14        