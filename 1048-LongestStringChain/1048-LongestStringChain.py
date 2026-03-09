# Last updated: 3/9/2026, 10:07:13 AM
1class Solution:
2    def longestStrChain(self, words: List[str]) -> int:
3        words.sort(key=len)
4        dp = {}
5        max_chain = 0
6        for word in words:
7            dp[word] = 1
8            for i in range(len(word)):
9                prev_word = word[:i] + word[i+1:]
10                if prev_word in dp:
11                    dp[word] = max(dp[word], dp[prev_word] + 1)
12            max_chain = max(max_chain, dp[word])
13        return max_chain