# Last updated: 3/7/2026, 9:42:30 AM
1class Solution:
2    def maximalSquare(self, matrix: List[List[str]]) -> int:
3    
4        m, n = len(matrix), len(matrix[0])
5
6        dp = [[0] * n for _ in range(m)] # mxn dynamic matrix
7
8        max_size = 0
9
10        for i in range(m):
11            for j in range(n):
12                if matrix[i][j] == '1':
13                    if i == 0 or j == 0:
14                        dp[i][j] =1
15                    else:
16                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
17                    max_size = max(max_size, dp[i][j])
18        return max_size*max_size