# Last updated: 2/26/2026, 5:50:02 PM
class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        base = int(s,2)
        steps = 0

        while base !=1:
            if base % 2 == 0:
                base = base//2
                steps +=1
            else:
                base +=1
                steps +=1
        return steps