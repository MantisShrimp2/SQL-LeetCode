# Last updated: 3/5/2026, 11:49:20 AM
1class Solution(object):
2    def minOperations(self, s):
3        """
4        :type s: str
5        :rtype: int
6        """
7        count_0 = 0
8        count_1 = 0
9
10        for i, char in enumerate(s):
11            if i % 2 ==0:
12                if char == '0':
13                    count_1 +=1
14                else:
15                    count_0 +=1
16        
17            else:
18                if char == '1':
19                    count_1 +=1
20                else:
21                    count_0 +=1
22
23        return min(count_0,count_1)
24            