class Solution:
    def minimumOperations(self, nums):
        count = 0
        
        while 0 in nums:
            nums.remove(0)
        
        while nums:
            x = min(nums)
            count += 1
            
            for i in range(len(nums)):
                nums[i] -= x
            
            while 0 in nums:
                nums.remove(0)
        
        return count