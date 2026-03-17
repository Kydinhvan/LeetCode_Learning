# Last updated: 3/17/2026, 3:02:07 PM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        # nums in list -> 2 numbers add to target
4        # iterate nums -> check one by one, if target minus curr in seen hash O(n)
5        # seen = {ele : index}
6        seen = {}
7        for i in range(len(nums)):
8            if target - nums[i] in seen:
9                return [i,seen[target - nums[i]]]
10            seen[nums[i]] = i
11
12        
13        
14
15        