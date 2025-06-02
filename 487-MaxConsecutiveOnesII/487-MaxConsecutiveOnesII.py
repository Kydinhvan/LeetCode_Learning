# Last updated: 6/2/2025, 9:24:44 PM
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # constrain 1 flip (0->1)
        # type, sliding window
        # Expand right pointer to explore.
        # Shrink left pointer only when the window violates the constraint.
        # Track window size with right - left + 1 whenever the window is valid.
        left = 0
        zero_count = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
        

