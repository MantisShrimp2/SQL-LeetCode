# Last updated: 2/26/2026, 12:30:25 PM
1class Solution(object):
2    def canConstruct(self, ransomNote, magazine):
3        """
4        :type ransomNote: str
5        :type magazine: str
6        :rtype: bool
7        """
8
9        mag_dict = {}
10        
11        for c in magazine:
12            if c not in mag_dict:
13                #count how many times each letter is in magazine
14                mag_dict[c] = 1
15            else:
16                mag_dict[c] +=1
17            
18        for r in ransomNote:
19            if r in mag_dict and mag_dict[r] >0:
20                mag_dict[r] -=1
21            else:
22                return False
23        return True
24