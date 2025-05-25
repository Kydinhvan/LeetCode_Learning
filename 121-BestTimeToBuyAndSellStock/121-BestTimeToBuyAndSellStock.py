# Last updated: 5/25/2025, 9:29:36 PM
class Solution(object):
    
    def maxProfit(self, prices):
        # identify sub problem cases
        # day with lowest price so far?
        # today price minus lowest price so far = max? 
        memo = {}
        def dp(i , minsofar):
            if (i , minsofar) in memo:
                return memo[(i , minsofar)]
            if i == len(prices):
                memo[(i , minsofar)] = 0
                return 0
            else:
                minsofar = min(prices[i],minsofar)
                maxprofit = max(prices[i]-minsofar,dp(i+1, minsofar))
                memo[(i, minsofar)] = maxprofit
            return maxprofit
        return dp(0,9999)
                 
        
        
        
        