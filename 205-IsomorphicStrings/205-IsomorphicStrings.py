# Last updated: 3/1/2026, 4:39:37 PM
1class Solution(object):
2    def wordPattern(self, pattern, s):
3        arr = s.split()
4        if len(arr) != len(pattern):
5            return False
6        
7        for i in range(len(arr)):
8            if pattern.find(pattern[i]) != arr.index(arr[i]):
9                return False
10        return True
11        