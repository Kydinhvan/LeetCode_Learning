# Last updated: 3/20/2026, 4:22:11 PM
1class Solution(object):
2    def numIslands(self, grid):
3        """
4        :type grid: List[List[str]]
5        :rtype: int
6        """
7    # given adj_matrix
8    # i will do a nested loop to ensure all node visited
9    # we ignore 0 and increase count whenever there is 1, then dfs to find the whole island
10    # to make sure we dont count the same island multiple, dfs will set 1 -> 0
11    
12        count = 0
13        rows = len(grid)
14        cols = len(grid[0])
15
16        def dfs(row, col):
17            # check boundary (base case)
18                # if 0 or out of bound, return
19            if row >= rows or col >= cols or row < 0 or col < 0 or grid[row][col] == "0" :
20                return
21            
22            # convert 1 -> 0
23            
24            grid[row][col] = "0"
25            # from current node, move in 4 directions
26
27            dfs(row + 1,col)
28            dfs(row - 1,col)
29            dfs(row,col - 1)
30            dfs(row,col + 1)
31        
32        for row in range(rows):
33            for col in range(cols):
34                if grid[row][col] == "1":
35                    dfs(row, col)
36                    count += 1
37
38        return count
39
40        
41
42    
43
44