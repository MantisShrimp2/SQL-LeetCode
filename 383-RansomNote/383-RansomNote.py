# Last updated: 2/26/2026, 12:30:49 PM
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        mag_dict = {}
        
        for c in magazine:
            if c not in mag_dict:
                #count how many times each letter is in magazine
                mag_dict[c] = 1
            else:
                mag_dict[c] +=1
            
        for r in ransomNote:
            if r in mag_dict and mag_dict[r] >0:
                mag_dict[r] -=1
            else:
                return False
        return True
