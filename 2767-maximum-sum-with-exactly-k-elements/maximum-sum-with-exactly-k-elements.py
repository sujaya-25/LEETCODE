class Solution(object):
    def maximizeSum(self, nums, k):
        m = max(nums)
        s = 0
        for i in range(k):
            s += m + i
        return s