# Last updated: 1/22/2026, 12:13:10 PM
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        seen = set()
        for i in range(n):
            seen.add(i)
            for e in range(n):
                if e in seen:
                    continue
                sum_of_num = nums[i] + nums[e]
                if sum_of_num == target:
                    return [i,e]
            

        