# Last updated: 3/5/2026, 12:15:07 PM
1import heapq
2class Solution(object):
3    def shortestDistance(self, maze, start, destination):
4        """
5        :type maze: List[List[int]]
6        :type start: List[int]
7        :type destination: List[int]
8        :rtype: int
9        """
10        row = len(maze)
11        col = len(maze[0])
12
13        moves = [[0,1], [0,-1],[1,0],[-1,0]] # up down, left right
14
15
16        visit = {}
17        visit[tuple(start)] = 0
18        min_heap = [(0, start[0], start[1])]
19        relaxed = set()
20
21        while min_heap:
22            dist, x, y = heapq.heappop(min_heap)
23            if [x,y] == destination:
24                return dist
25
26            
27            if (x,y) in relaxed:
28                continue
29            else: 
30                relaxed.add((x,y))
31                x1, y1 = x,y
32                for dx, dy in moves:
33                    count = 0
34                    while 0 <= x1 + dx < row and 0 <= y1 + dy < col and maze[x1 + dx][y1 + dy] != 1:
35                        x1 += dx
36                        y1 += dy
37                        count +=1
38                    if (x1, y1) not in visit or visit[(x1, y1)] > dist + count:
39                        visit[(x1, y1)] = dist + count
40                        heapq.heappush(min_heap, (dist + count, x1, y1))
41                    x1, y1 = x, y
42        return -1
43
44        
45        