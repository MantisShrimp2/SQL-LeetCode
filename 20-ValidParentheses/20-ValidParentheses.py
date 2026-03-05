# Last updated: 3/5/2026, 4:13:42 PM
1class Solution(object):
2    def isValid(self, s):
3        """
4        :type s: str
5        :rtype: bool
6        """
7        stack = []
8
9        bracket = {'(':')', '[':']','{':"}"}
10        
11
12        for char in s:
13            if char in bracket:
14                stack.append(char)
15            elif len(stack) == 0 or bracket[stack.pop()] != char:
16                return False
17        return len(stack) == 0
18            
19            
20    