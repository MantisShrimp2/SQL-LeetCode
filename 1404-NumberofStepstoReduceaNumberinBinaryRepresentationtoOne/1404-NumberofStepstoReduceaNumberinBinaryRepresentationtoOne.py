# Last updated: 2/26/2026, 5:49:09 PM
class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        c=0
        
        num=int(s,2)
        while(num!=1):
            if((num&1)==1):
                num+=1
                c+=1
            else:
                num=num>>1
                c+=1
        return c