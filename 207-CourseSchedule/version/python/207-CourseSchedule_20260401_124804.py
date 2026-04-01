# Last updated: 4/1/2026, 12:48:04 PM
1class Solution:
2    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
3        # [ai, bi] -> ai need b1
4        # num_course = 6, [[0,1][1,2][2,3][3,0]]
5        # 0: 1,5
6        # 1: 2,3
7        # 2: 3
8        # 3: 0 <- cycle
9        # 4:
10        # 5: 
11
12        # dict for graph 
13        # [0,1,2,3,0] <- cycle
14
15        graph = {}
16        for i in range(numCourses): # empty list of prereq, even for empty one
17            graph[i] = []
18
19        for course, pre_req in prerequisites:
20            if course in graph:
21                graph[course].append(pre_req)
22            else:
23                graph[course] = [pre_req]
24
25        stack = set()
26        visited = set()
27        
28        def dfs(course) -> bool:
29            # stack -> cycle; visited -> skip
30            # add stack 
31            # go thru all the pre_req in list 
32            # remove from stack 
33            # add to visited
34            # base 
35
36            if course in stack:
37                return True # has cycle
38
39            if course in visited: #O(1)
40                return False # done and no cycle
41
42            stack.add(course)
43            
44            for pre_req in graph[course]:
45                res = dfs(pre_req)
46                if res: #cycle
47                    return True                
48
49            stack.remove(course)
50            visited.add(course)
51            return False
52
53        for course, pre_list in graph.items():
54            result = dfs(course)
55
56            if result: # cycle
57                return False
58        return True