class Solution(object):
    def maxSubArray(self, nums):
        m = nums[0]
        s = nums[0]
        
        for i in range(1, len(nums)):
            if s >= 0:
                s = s + nums[i]
            else:
                s = nums[i]
            
            if m < s:   
                m = s
        
        return m