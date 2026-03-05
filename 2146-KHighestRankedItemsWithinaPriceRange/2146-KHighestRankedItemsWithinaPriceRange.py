# Last updated: 3/5/2026, 12:33:42 PM
from collections import deque

class Solution(object):
    def highestRankedKItems(self, grid, pricing, start, k):
        m, n = len(grid), len(grid[0])
        low, high = pricing
        
        visited = [[False]*n for _ in range(m)]
        q = deque()
        q.append((start[0], start[1], 0))
        visited[start[0]][start[1]] = True
        
        items = []
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while q:
            r, c, d = q.popleft()
            val = grid[r][c]
            
            if low <= val <= high and val > 1:
                items.append((d, val, r, c))
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] != 0:
                    visited[nr][nc] = True
                    q.append((nr, nc, d + 1))
        
        items.sort()
        return [[r, c] for _, _, r, c in items[:k]]

        