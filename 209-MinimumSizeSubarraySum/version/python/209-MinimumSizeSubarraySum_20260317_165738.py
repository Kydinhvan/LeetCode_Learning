# Last updated: 3/17/2026, 4:57:38 PM
1class Solution(object):
2    def minSubArrayLen(self, target, nums):
3        """
4        :type target: int
5        :type nums: List[int]
6        :rtype: int
7        """
8        # min len of sub-array -> sum(subarr) = target, else -> 0
9        # iterate with a window, right left pointer
10        # expand (right) if sum <= target, else shrink (left-1) till sum <= target
11        # if equal to target, get min_count
12        min_count = float('inf')
13        left = 0
14        sub_arr_sum = 0
15        for right in range(len(nums)):
16            sub_arr_sum += nums[right]
17
18            while sub_arr_sum >= target:
19                min_count = min(min_count, right-left +1)
20                sub_arr_sum -= nums[left]
21                left += 1
22        
23        if min_count == float('inf'):
24            return 0
25
26        return min_count
27        