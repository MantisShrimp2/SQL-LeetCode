# Last updated: 2/28/2026, 5:25:48 PM
1class Solution(object):
2    def isPalindrome(self, s):
3        """
4        :type s: str
5        :rtype: bool
6        """
7        #convert 
8        s = [c.lower() for c in s if c.isalnum()]
9
10        
11        return s == s[::-1]