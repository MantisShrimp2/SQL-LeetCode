# Last updated: 2/26/2026, 12:30:50 PM
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #first check negative numbers;
        if x < 0 or (x % 10  == 0 and x !=0):
            return False
        
        temp = x
        rev = 0 #reverse
        while temp > 0:
            num = temp % 10
            rev = rev * 10 + num
            temp = temp // 10
        return rev == x


        