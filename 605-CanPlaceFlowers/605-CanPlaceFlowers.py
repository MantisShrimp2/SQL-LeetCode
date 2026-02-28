# Last updated: 2/28/2026, 11:18:19 AM
1class Solution(object):
2    def canPlaceFlowers(self, flowerbed, n):
3        """
4        :type flowerbed: List[int]
5        :type n: int
6        :rtype: bool
7        """
8        for i in range(len(flowerbed)):
9            left = (i ==0 ) or  (flowerbed[i-1] ==0 )
10            right = (i == len(flowerbed)-1)  or (flowerbed[i+1] == 0)
11
12            if flowerbed[i] == 0 and left and right:
13                flowerbed[i]  = 1
14                n -=1
15        return n <=0 