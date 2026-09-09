class Solution(object):
    def maxFrequencyElements(self, nums):
        freq={}
        c=0
        for i in nums:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        m=max(freq.values())
        for k in freq:
            if freq[k]==m:
                c=c+freq[k]
        return(c)