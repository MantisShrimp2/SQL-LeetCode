# Last updated: 3/2/2026, 6:43:30 PM
1class Solution(object):
2    def rotate(self, matrix):
3        """
4        :type matrix: List[List[int]]
5        :rtype: None Do not return anything, modify matrix in-place instead.
6        """
7        matrix.reverse()
8        for i in range(len(matrix)):
9            for j in range(i):
10                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]