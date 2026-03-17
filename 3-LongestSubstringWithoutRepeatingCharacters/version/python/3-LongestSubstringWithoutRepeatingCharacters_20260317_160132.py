# Last updated: 3/17/2026, 4:01:32 PM
1class Solution(object):
2    def lengthOfLongestSubstring(self, s):
3        """
4        :type s: str
5        :rtype: int
6        """
7        # given string -> substring with longest unique char
8        # iterate with 2 pointers, if right pointer expand as long as substring no dup
9        # left strink when there are dup, 
10        # keep max count, keep set of seen (to check for dup) this set contain current window
11        max_count = 1
12        seen = set()
13        left = 0
14        right = 1
15        
16        if len(s) == 0:
17            return 0
18
19        seen.add(s[left])
20        for i in range(len(s)-1):
21            while s[right] in seen: # as long as there is still dup, move 
22                seen.remove(s[left]) 
23                left += 1
24            seen.add(s[right])
25            right += 1
26            
27            max_count = max(max_count, right-left)
28        return max_count
29
30
31