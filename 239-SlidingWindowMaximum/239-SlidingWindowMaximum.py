# Last updated: 3/3/2026, 9:25:56 AM
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()  # stores indices
        result = []

        for i in range(len(nums)):

            # Remove indices out of current window
            if dq and dq[0] == i - k:
                dq.popleft()

            # Remove smaller elements from back
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # Start adding to result after first window
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result