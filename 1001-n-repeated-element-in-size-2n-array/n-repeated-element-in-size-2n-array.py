class Solution(object):
    def repeatedNTimes(self, nums):
        freq={}
        for i in nums:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        for key in freq:
            if freq[key]>1:
                return key
        