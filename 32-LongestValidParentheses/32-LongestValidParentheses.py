# Last updated: 3/6/2026, 11:06:18 AM
1class Solution(object):
2    def longestValidParentheses(self, s):
3        """
4        :type s: str
5        :rtype: int
6        """
7        stack = []
8        l = ['0']*len(s)
9        for i, char in enumerate(s):
10            if char == '(':
11                stack.append(i)
12            else:
13                if stack:
14                    l[stack.pop()] = '1'
15                    l[i] = '1'
16        return max(len(i) for i in ''.join(l).split('0'))