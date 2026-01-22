# Last updated: 1/22/2026, 12:12:46 PM
class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # moving window to get maximum number of consecutive 1 and 0 
        # zero count within a window < k
        # expand window right if valif, reduce left if invalid

        left = 0 
        max_count = 0
        count = 0
        zero_count = 0

        for right in range(len(nums)):
            if nums[right] == 1:
                count += 1 

            elif nums[right] == 0:
                zero_count += 1
                count += 1
                while zero_count > k:
                    if nums[left] == 0:
                        left += 1
                        count -= 1
                        zero_count -= 1
                    
                    elif nums[left] == 1:
                        left += 1
                        count -= 1            

            max_count = max(count,max_count)
        return max_count






            


            


