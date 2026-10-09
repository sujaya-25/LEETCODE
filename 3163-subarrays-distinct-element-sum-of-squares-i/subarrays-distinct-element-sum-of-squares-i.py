class Solution(object):
    def sumCounts(self, nums):
        freq={}
        p=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                sub=nums[i:j+1]
                s=set(sub)
                l=list(s)
                p+=len(l)**2
        return p




