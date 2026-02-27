# Last updated: 2/27/2026, 9:06:33 PM
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        translate = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000

        }
        num = 0
        #replcace numbers
        s = s.replace('IV','IIII') #4
        s = s.replace('IX','VIIII')#9
        s = s.replace('XL', 'XXXX')#40
        s = s.replace('XC', 'LXXXX')#90
        s = s.replace('CD', 'CCCC')#400
        s = s.replace('CM', 'DCCCC') #900

        for char in s:
            if char in translate:
                num += translate[char]
        return num