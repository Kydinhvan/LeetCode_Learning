# Last updated: 3/17/2026, 9:51:43 PM
1class Solution(object):
2    def isValid(self, s):
3        """
4        :type s: str
5        :rtype: bool
6        """
7        # stack -> last in first out
8        # iterate, append stack until a closing bracket seen
9        # if closing bracket not corresposne -> return false
10        # if stack not empty after iter -> return false. Else true
11        # 1, 2, 3 check
12        # ) 
13        stack = []
14        mapping = {")": "(", "}": "{", "]": "["}
15
16        for b in s:
17            if b in mapping:
18                if stack:
19                    top_ele = stack.pop()
20                else:
21                    return False
22
23                if mapping[b] != top_ele:
24                    return False
25            else:
26                stack.append(b)
27        if not stack:
28            return True
29        else:
30            return False