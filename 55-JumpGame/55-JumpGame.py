# Last updated: 2/28/2026, 12:50:19 PM
1class Solution(object):
2    def lengthOfLastWord(self, s):
3        """
4        :type s: str
5        :rtype: int
6        """
7
8        s_len = len(s)
9        word = []
10        for i in range(s_len-1, -1, -1):   # 4, 3, 2, 1, 0
11            if s[i] != ' ':
12                word.append(s[i])
13            elif word:
14                break
15        return len(word)
16        