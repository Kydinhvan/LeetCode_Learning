# Last updated: 6/2/2025, 5:45:01 PM
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # count +1 for every step
        # save max_count
        # cases: all 1 
        max_count = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1: # if current is 1 and update max
                count +=1
                if count > max_count:
                    max_count = count 
            else:
                count = 0
                
        return max_count
