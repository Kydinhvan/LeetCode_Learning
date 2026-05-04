# Last updated: 5/4/2026, 10:55:03 PM
1class Solution(object):
2    def maxAreaOfIsland(self, grid):
3        """
4        :type grid: List[List[int]]
5        :rtype: int
6        """
7        # [[row1],
8        #  [row2]]
9
10        # nested loop to check each cell
11        # if cell == 1, dfs horizontal or vertical 
12        # func dfs 
13        max_rows = len(grid)
14        max_cols = len(grid[0])
15        max_area = 0
16
17        def dfs(rows, cols):
18            if rows >= max_rows or cols >= max_cols or rows < 0 or cols < 0 or grid[rows][cols] == 0:
19                return 0
20            
21            
22            grid[rows][cols] = 0 # set like visited   
23            area = 1
24            area += dfs(rows,cols + 1)
25            area += dfs(rows,cols - 1)
26            area += dfs(rows + 1, cols)
27            area += dfs(rows - 1, cols)
28            return area
29
30
31        for rows in range(len(grid)):
32            for cols in range(len(grid[rows])):
33                if grid[rows][cols] == 1:
34                    count = 0
35                    curr_curr = dfs(rows,cols)
36                    print(curr_curr)
37                    max_area = max(curr_curr,max_area)
38
39
40        return max_area
41
42
43            