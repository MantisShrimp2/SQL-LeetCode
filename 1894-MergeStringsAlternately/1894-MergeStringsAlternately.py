# Last updated: 2/28/2026, 6:04:22 PM
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = ''

        n = min(len(word1), len(word2))

        for i in range(n):
            result +=word1[i] + word2[i]
        if len(word1) > len(word2):
            result += word1[n:]
        else:
            result += word2[n:]
        return result
