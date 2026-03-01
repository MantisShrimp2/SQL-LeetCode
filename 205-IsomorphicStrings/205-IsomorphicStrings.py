# Last updated: 3/1/2026, 4:37:02 PM
1class Solution(object):
2    def isIsomorphic(self, s, t):
3        """
4        :type s: str
5        :type t: str
6        :rtype: bool
7        """
8        zipped = set(zip(s,t))
9        return len(zipped) == len(set(s)) == len(set(t))