# Last updated: 3/23/2026, 10:56:07 PM
# Need to try again
1class Solution(object):
2    def canFinish(self, numCourses, prerequisites):
3        """
4        :type numCourses: int
5        :type prerequisites: List[List[int]]
6        :rtype: bool
7        """
8    # numCourses -> 2, min num course needed -> must have at least 2 course can take
9    # preeq -> 2d array [[1,0],[0,1]]
10    # graph problem -> directed, cycle dectection
11    # 1 -> 0; 0 -> 1 (cycle detected)
12    
13
14    # cycle detection problem, use stack for current_path, if curr_node in curr_path
15
16    # graph = {
17    #    1: 0,
18    #    2: 3
19    #}
20
21    # convert to graph
22        graph = {}
23        visited = set() # fast look up
24        curr_stack = set()
25        
26        graph = {i:[] for i in range(numCourses)}
27        for course, pre in prerequisites:
28            graph[pre].append(course) # pre_req: course
29        # {0: [1], 1: []}
30        
31        def dfs(course):
32
33            # base case
34            if course in curr_stack:
35                return False # cycle
36
37            if course in visited:
38                return True # checked, skip ahead
39            
40            visited.add(course)
41            curr_stack.add(course)
42
43            for nei in graph[course]:
44                if not dfs(nei): # not visited
45                    return False # enter if course in curr_stack True
46
47            curr_stack.remove(course)
48            return True
49
50        for courses in range(numCourses):
51            if not dfs(courses):
52                return False
53
54        return True
55
56
57    # traverse using dfs
58    
59    # dfs
60    
61    # [1,2,3,5,1] -> true