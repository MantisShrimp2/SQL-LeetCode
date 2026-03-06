# Last updated: 3/6/2026, 7:25:58 PM
1class Solution:
2    def plusOne(self, digits: List[int]) -> List[int]:
3        
4        n = len(digits)   
5        for i in range(n-1, -1, -1):
6
7            if digits[i] == 9:
8                digits[i] = 0
9            else:
10                digits[i] = digits[i] + 1
11                return digits
12        return [1] + digits
13        