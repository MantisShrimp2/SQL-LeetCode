# Last updated: 2/26/2026, 5:48:32 PM
1class Solution(object):
2    def numSteps(self, s):
3        """
4        :type s: str
5        :rtype: int
6        """
7        base = int(s,2)
8        steps = 0
9
10        while base !=1:
11            if base % 2 == 0:
12                base = base//2
13                steps +=1
14            else:
15                base +=1
16                steps +=1
17        return steps