# Last updated: 2/5/2026, 6:02:01 PM
# heapheap
1import heapq
2class Solution:
3    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
4        # max_active_room
5        # treat meeting room as min heap with root as ending soon room
6        # count len of heap each iter
7        
8        # sort all meeting by start
9        # init min heap
10        # push first meeting in heap
11
12        # iter thru the remainding room:
13            # if start_i > end_i-1 -> remove from heap
14                # heap push current meeting 
15
16        # return
17
18        s_list = sorted(intervals)
19        active_room = []
20        heapq.heappush(active_room, s_list[0][1])
21
22        for i in range(1,len(s_list)):
23            if s_list[i][0] >= active_room[0]:
24                heapq.heappop(active_room)
25                heapq.heappush(active_room, s_list[i][1])
26            else:
27                heapq.heappush(active_room, s_list[i][1])
28
29        return len(active_room)
30            