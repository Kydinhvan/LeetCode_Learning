# Last updated: 1/22/2026, 12:13:09 PM
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # brute force
        # at every step/level, take either 1 and 2
        # use dict to record previously computed step
        computed = {}
        return self.climb_Stairs(0,n,computed)

    def climb_Stairs(self,i,n,computed):
        if i > n:
            return 0
        elif i == n:
            return 1
        if i in computed:
            return computed[i]
        computed[i] = self.climb_Stairs(i + 1,n,computed) + self.climb_Stairs(i + 2,n,computed)

        return computed[i]
