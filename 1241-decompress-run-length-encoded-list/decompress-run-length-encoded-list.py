class Solution(object):
    def decompressRLElist(self, nums):
        a=[]
        for i in range(0,len(nums),2):
            sub=nums[i:i+2]
            freq=sub[0]
            key=sub[1]
            for j in range(freq):
                a.append(key)     
        return a   