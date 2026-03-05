# Last updated: 3/5/2026, 4:38:44 PM
1class Solution(object):
2    def trap(self, height):
3        """
4        :type height: List[int]
5        :rtype: int
6        """
7        n = len(height)
8        left, right = [0] * n , [0] * n
9        water = 0
10
11        if len(height) == 0:
12            return 0
13
14        left[0] = height[0] 
15        for i in range(1,n):
16            left[i] = max(left[i-1], height[i])
17
18        right[n-1] = height[n-1]
19        for i in range(n-2, -1, -1):
20            right[i] = max(right[i+ 1], height[i])
21
22        for i in range(n):
23            water += min(left[i], right[i]) - height[i]
24
25        return water
26
27
28
29
30
31        
32