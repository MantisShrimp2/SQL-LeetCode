# Last updated: 3/6/2026, 11:59:21 AM
class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        count_0 = 0
        count_1 = 0

        for i, char in enumerate(s):
            if i % 2 ==0:
                if char == '0':
                    count_1 +=1
                else:
                    count_0 +=1
        
            else:
                if char == '1':
                    count_1 +=1
                else:
                    count_0 +=1

        return min(count_0,count_1)
            