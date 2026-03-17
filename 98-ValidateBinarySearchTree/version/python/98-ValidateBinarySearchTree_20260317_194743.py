# Last updated: 3/17/2026, 7:47:43 PM
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7from collections import deque
8class Solution(object):
9    def isValidBST(self, root):
10        """
11        :type root: Optional[TreeNode]
12        :rtype: bool
13        """
14        # queue = deque([(root, float('-inf'), float('inf'))])
15        #- the problem sounds like recursion but it can also be solved with a queue 1. queue start with root in it -> queue will be each level 2. iterate thru each level -> ensure root< left and root>right. 
16        #problem doesnt mention equal case so i will assume  root>-right. 
17# while q loop to traverse all level, each iter is 1 level, for loop q to make sure one iter is one level
18# for each iter of while loop, pass down max and min of that level pass down using queue
19        
20        # at least root is present
21        if root.left is None and root.right is None:
22            return True
23        
24        q = deque([(root, float('-inf'), float('inf'))])
25
26        while q:
27            for _ in range(len(q)):
28                curr_node, min_lim, max_lim = q.popleft()
29                if min_lim >= curr_node.val or max_lim <= curr_node.val: # invalid
30                    return False
31                
32                # pass down info
33                if curr_node.left:
34                    q.append((curr_node.left,min_lim, curr_node.val)) # push left node with updated upper lim
35                if curr_node.right:
36                    q.append((curr_node.right,curr_node.val,max_lim)) # push right node with updated lower lim
37
38        return True