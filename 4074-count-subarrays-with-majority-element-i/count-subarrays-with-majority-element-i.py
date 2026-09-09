class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        c = 0
        
        for i in range(len(nums)):
            count = 0   
            
            for j in range(i, len(nums)):
                
                if nums[j] == target:   
                    count += 1
                
                length = j - i + 1
                
                if count > length // 2:
                    c += 1
        
        return c