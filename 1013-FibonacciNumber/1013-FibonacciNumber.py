# Last updated: 1/22/2026, 12:12:48 PM
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # save result in a list
        if n <= 1:
            return n
        dp = [0] * (n+1)
        dp[1] = 1

        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]
        