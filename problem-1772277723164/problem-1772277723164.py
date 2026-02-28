# Last updated: 2/28/2026, 12:22:03 PM
1class Solution(object):
2    def maxProfit(self, prices):
3        """
4        :type prices: List[int]
5        :rtype: int
6        """
7        if not prices:
8            return 0
9
10        profit = 0
11        for i in range(1, len(prices)):
12            if prices[i] > prices[i - 1]:
13                profit += prices[i] - prices[i - 1]
14        return profit