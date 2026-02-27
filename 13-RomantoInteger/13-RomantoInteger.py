# Last updated: 2/27/2026, 8:57:25 PM
1class Solution(object):
2    def romanToInt(self, s):
3        """
4        :type s: str
5        :rtype: int
6        """
7        translate = {
8            'I':1,
9            'V':5,
10            'X':10,
11            'L':50,
12            'C':100,
13            'D':500,
14            'M':1000
15
16        }
17        num = 0
18        #replcace numbers
19        s = s.replace('IV','IIII') #4
20        s = s.replace('IX','VIIII')#9
21        s = s.replace('XL', 'XXXX')#40
22        s = s.replace('XC', 'LXXXX')#90
23        s = s.replace('CD', 'CCCC')#400
24        s = s.replace('CM', 'DCCCC') #900
25
26        for char in s:
27            if char in translate:
28                num += translate[char]
29        return num