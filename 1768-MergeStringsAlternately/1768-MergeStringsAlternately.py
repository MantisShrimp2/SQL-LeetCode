# Last updated: 2/28/2026, 10:39:21 AM
1class Solution(object):
2    def mergeAlternately(self, word1, word2):
3        """
4        :type word1: str
5        :type word2: str
6        :rtype: str
7        """
8        result = ''
9
10        n = min(len(word1), len(word2))
11
12        for i in range(n):
13            result +=word1[i] + word2[i]
14        if len(word1) > len(word2):
15            result += word1[n:]
16        else:
17            result += word2[n:]
18        return result
19