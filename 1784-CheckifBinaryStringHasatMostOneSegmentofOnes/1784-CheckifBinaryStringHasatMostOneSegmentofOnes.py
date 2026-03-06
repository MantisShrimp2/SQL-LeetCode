# Last updated: 3/6/2026, 9:11:31 AM
1class Solution(object):
2    def checkOnesSegment(self, s):
3        """
4        :type s: str
5        :rtype: bool
6        """
7        n = len(s)
8        if len(s) == 1:
9            return True
10        
11        for i in range(0,n-1):
12            c1 = s[i]
13            c2 = s[i+1]
14            if c1 == '0' and c2 == '1':
15                return False
16        return True