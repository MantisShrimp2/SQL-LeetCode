# Last updated: 3/6/2026, 11:59:30 AM
import heapq
class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        row = len(maze)
        col = len(maze[0])

        moves = [[0,1], [0,-1],[1,0],[-1,0]] # up down, left right


        visit = {}
        visit[tuple(start)] = 0
        min_heap = [(0, start[0], start[1])]
        relaxed = set()

        while min_heap:
            dist, x, y = heapq.heappop(min_heap)
            if [x,y] == destination:
                return dist

            
            if (x,y) in relaxed:
                continue
            else: 
                relaxed.add((x,y))
                x1, y1 = x,y
                for dx, dy in moves:
                    count = 0
                    while 0 <= x1 + dx < row and 0 <= y1 + dy < col and maze[x1 + dx][y1 + dy] != 1:
                        x1 += dx
                        y1 += dy
                        count +=1
                    if (x1, y1) not in visit or visit[(x1, y1)] > dist + count:
                        visit[(x1, y1)] = dist + count
                        heapq.heappush(min_heap, (dist + count, x1, y1))
                    x1, y1 = x, y
        return -1

        
        