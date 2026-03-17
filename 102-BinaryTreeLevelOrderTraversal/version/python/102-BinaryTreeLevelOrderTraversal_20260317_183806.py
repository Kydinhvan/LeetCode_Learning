# Last updated: 3/17/2026, 6:38:06 PM
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8from collections import deque
9class Solution(object):
10    def levelOrder(self, root):
11        """
12        :type root: Optional[TreeNode]
13        :rtype: List[List[int]]
14        """
15        # need a queue. Start with the root in it
16        # iterate thru each level -> add to output list at the end
17        # get len(q) at start of each iter -> everything added after will be children for next iter
18        output = []
19        if root is None:
20            return output
21        q = deque([root])
22        
23        while q: # q will be empty when there is no more child node
24            level = []
25            for _ in range(len(q)): 
26                node = q.popleft()
27                level.append(node.val)
28                #addchild
29                if node.left:
30                    q.append(node.left)
31                if node.right:
32                    q.append(node.right)
33            
34            output.append(level)
35
36 
37        return output
38
39
40
41
42        