# Last updated: 2/27/2026, 3:23:50 PM
1class Solution(object):
2    def myPow(self, x, n):
3        """
4        :type x: float
5        :type n: int
6        :rtype: float
7        """
8        if n == 0:
9            return 1.0
10        if n <0:
11            x  = 1/x
12            n = -n
13        half = self.myPow(x,n//2)
14
15        if n % 2 == 0:
16            return half * half
17        else:
18            return half * half * x
19            
20