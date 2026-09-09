class Solution(object):
    def minSubArrayLen(self, target, nums):
        s=0
        m=len(nums)+1
        i=0

        for j in range(len(nums)):
            s=s+nums[j]

            while s>=target:
                m=min(m,j-i+1)
                s=s-nums[i]
                i=i+1

        if m==len(nums)+1:
            return 0
        return m