class Solution(object):
    def sortedSquares(self, nums):
        a=[]
        for i in range(len(nums)):
            a.append(nums[i]*nums[i])
        a.sort()
        return a        