class Solution(object):
    def countElements(self, nums):
        c=0
        for i in range(len(nums)):
            if nums[i]>min(nums) and nums[i]<max(nums):
                c+=1
        return c
        