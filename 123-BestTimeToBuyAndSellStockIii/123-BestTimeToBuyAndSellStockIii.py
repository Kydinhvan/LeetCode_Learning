# Last updated: 1/22/2026, 12:13:04 PM
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # bruteforce: 2 most profitable sequential b1 < s1 < b2 < s2 O(n^4)
        # sell every day buy chepeast from both side
        # (this give us best 1st and 2nd trade)
        # from right, max - current price
        # with 2 table, iterate through 2 list 
        # dp stored max profit possible (0...i)
        max_profit = 0
        n = len(prices)
        min_1 = prices[0]
        max_2 = prices[-1]

        dp_1 = [0] * (n+1)
        dp_2 = [0] * (n+1)

        for i in range(1,n):
            dp_1[i] = max(prices[i] - min_1, dp_1[i-1])
            min_1 = min(prices[i],min_1)

        for e in range(n-1,0,-1):
            dp_2[e] = max(max_2 - prices[e], dp_2[e+1]) # e start n - 1
            max_2 = max(prices[e],max_2)

        for x in range(n):
            max_profit = max(dp_1[x]+dp_2[x+1], max_profit)

        return max_profit





            
            





        return max_profit
        
        