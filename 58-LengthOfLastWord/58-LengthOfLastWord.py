# Last updated: 2/28/2026, 6:04:37 PM
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        s_len = len(s)
        word = []
        for i in range(s_len-1, -1, -1):   # 4, 3, 2, 1, 0
            if s[i] != ' ':
                word.append(s[i])
            elif word:
                break
        return len(word)
        