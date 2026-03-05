# Last updated: 3/5/2026, 5:00:42 PM
1class Solution(object):
2    def numWaterBottles(self, numBottles, numExchange):
3        """
4        :type numBottles: int
5        :type numExchange: int
6        :rtype: int
7        """
8        canDrink = numBottles
9
10        while numBottles >= numExchange:
11                numBottles -= (numExchange -1)
12                canDrink += 1
13        return canDrink