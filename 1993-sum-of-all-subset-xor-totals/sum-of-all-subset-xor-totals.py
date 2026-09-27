class Solution(object):
    def subsetXORSum(self, nums):
        a=[0]
        for i in nums:
            for j in range(len(a)):
                a.append(a[j]^i)
        return sum(a)