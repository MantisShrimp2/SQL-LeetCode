# Last updated: 3/6/2026, 11:59:20 AM
class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        if len(s) == 1:
            return True
        
        for i in range(0,n-1):
            c1 = s[i]
            c2 = s[i+1]
            if c1 == '0' and c2 == '1':
                return False
        return True