class Solution(object):
    def minOperations(self, nums):
        count=0
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                a=nums[i-1]+1-nums[i]
                count+=a
                nums[i]=nums[i-1]+1
        return count