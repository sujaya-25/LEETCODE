class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        a=[]
        s=0
        for i in range(len(nums)):
            a.append(bin(i)[2:])
        for i in range(len(a)):
            if a[i].count('1')==k:
                s+=nums[i]
        return s
        