# Last updated: 2/26/2026, 11:32:11 AM
class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        top_wealth = 0.0
        for i in range (len(accounts)):
            netwealth = sum(accounts[i])
            top_wealth = max(netwealth, top_wealth)
        return top_wealth

        
        