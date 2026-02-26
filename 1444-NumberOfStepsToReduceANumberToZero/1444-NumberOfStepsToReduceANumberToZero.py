# Last updated: 2/26/2026, 11:32:13 AM
class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        steps = 0
        while num != 0:
            if num % 2 == 0:
                #if even
                num = num //2
                steps +=1
            else:
                #if odd:
                num = num-1
                steps +=1
        if num == 0:
            return steps