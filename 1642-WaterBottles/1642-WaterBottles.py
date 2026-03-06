# Last updated: 3/6/2026, 11:59:24 AM
class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        canDrink = numBottles

        while numBottles >= numExchange:
                numBottles -= (numExchange -1)
                canDrink += 1
        return canDrink