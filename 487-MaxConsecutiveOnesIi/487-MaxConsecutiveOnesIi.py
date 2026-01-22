# Last updated: 1/22/2026, 12:12:54 PM
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sliding window
        # expand right if valid
        # strink left if more than 1 zero in the window until less than one window

        left = 0
        max_len = 0
        count = 0
        zero_count = 0

        for right in range(len(nums)):
            if nums[right] == 1:
                count += 1
            
            elif nums[right] == 0: 
                zero_count += 1
                count += 1
                while zero_count > 1: # check for invalid window
                    if nums[left] == 0:
                        zero_count -= 1
                    left += 1
                    count -= 1


            max_len = max(max_len, count)
        return max_len
            


