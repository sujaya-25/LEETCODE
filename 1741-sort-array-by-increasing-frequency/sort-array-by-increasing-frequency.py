class Solution(object):
    def frequencySort(self, nums):
        freq={}
        
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if freq[nums[i]]>freq[nums[j]]:
                    nums[i],nums[j]=nums[j],nums[i]
                elif freq[nums[i]]==freq[nums[j]] and nums[i]<nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]
        
        return nums