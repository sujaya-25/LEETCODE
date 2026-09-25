class Solution(object):
    def smallestIndex(self, nums):
        for i in range(len(nums)):
            d=nums[i]
            s=0
            while d>0:
                s+=d%10
                d=d//10
            if s==i:
                return i
        return -1


        