# Last updated: 3/3/2026, 9:16:07 AM
1class Solution:
2    def maxSlidingWindow(self, nums, k):
3        window = []  
4        result = []
5
6        for i, num in enumerate(nums):
7
8            # Remove indices outside the current window
9            if window and window[0] < i - k + 1:
10                window.pop(0)
11
12            # Remove smaller elements from the back
13            while window and nums[window[-1]] < num:
14                window.pop()
15
16            window.append(i)
17
18            # Start adding results once first window is complete
19            if i >= k - 1:
20                result.append(nums[window[0]])
21
22        return result