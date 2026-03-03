# Last updated: 3/3/2026, 9:27:07 AM
class Solution(object):
    def wordPattern(self, pattern, s):
        arr = s.split()
        if len(arr) != len(pattern):
            return False
        
        for i in range(len(arr)):
            if pattern.find(pattern[i]) != arr.index(arr[i]):
                return False
        return True
        