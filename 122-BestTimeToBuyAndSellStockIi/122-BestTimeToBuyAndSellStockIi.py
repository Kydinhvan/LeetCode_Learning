# Last updated: 1/22/2026, 12:13:05 PM
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # cheapest and the immediate peak followed
        n = len(prices)
        max_profit = 0
        i = 0
        while i < n - 1:
            while i < n - 1 and prices[i+1] <= prices[i]: # downward trend
                i += 1
            cheapest = prices[i]

            while i < n - 1 and prices[i+1] >= prices[i]: # upward trend
                i += 1
            peak = prices[i]

            max_profit += peak - cheapest

        return max_profit


        
