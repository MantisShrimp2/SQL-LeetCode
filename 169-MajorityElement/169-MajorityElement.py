# Last updated: 2/26/2026, 4:21:51 PM
class Solution(object):
    def majorityElement(self, nums):
        d={}
        for i in nums:
            if i not in d.keys():
                d[i]=1
            else:
                d[i]+=1
        return max(d,key=d.get)

        