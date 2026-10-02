class Solution:
    def numberOfPairs(self, nums):
        count = 0
        for i in set(nums):
            count += nums.count(i) // 2
        
        return [count, len(nums) - count * 2]