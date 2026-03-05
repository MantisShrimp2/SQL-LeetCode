# Last updated: 3/5/2026, 12:30:06 PM
1import heapq
2class Solution:
3    def highestRankedKItems(self, grid, pricing, start, k):
4        row, col = len(grid), len(grid[0])
5        q = [(0, grid[start[0]][start[1]], start[0], start[1])] # the color map
6        visit = set()
7        result = []
8        while q:
9            dis, price, x, y = heapq.heappop(q)
10            if (x, y) in visit:
11                continue
12            visit.add((x, y))
13            if price != 1 and price >= pricing[0] and price <= pricing[1]:
14                result.append([x, y])
15            if len(result) == k:
16                return result
17            for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
18                new_x, new_y = x + dx, y + dy
19                if 0 <= new_x < row and 0 <= new_y < col and (new_x, new_y) not in visit:
20                    temp = grid[new_x][new_y]
21                    if temp == 0:
22                        continue
23                    elif temp == 1:
24                        heapq.heappush(q, (dis + 1, 1, new_x, new_y))
25                    else:
26                        heapq.heappush(q, (dis + 1, temp, new_x, new_y))
27        
28        return result