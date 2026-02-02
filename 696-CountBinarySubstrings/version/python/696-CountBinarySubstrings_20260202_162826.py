# Last updated: 2/2/2026, 4:28:26 PM
1class Solution(object):
2    def countBinarySubstrings(self, s):
3        """
4        :type s: str
5        :rtype: int
6        """
7        # return count of [sub str with same count of 0 and 1 consecutive]
8        # cannot be empty
9        # len(0) = len(1)
10        # "00110011" -> 0011 has 2, 1100 has 2
11        # "000110" -> 00011 has 2, 110 has 1
12
13        # constraint by min consecutive pair
14        group = []
15        count = 1
16
17        for i in range(1,len(s)):
18            if s[i] == s[i-1]:
19                count +=1
20
21            else:
22                group.append(count)
23                count = 1
24        group.append(count) 
25        result = 0
26        for i in range(1,len(group)):
27            result += min(group[i],group[i-1])
28
29        return result