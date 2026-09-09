class Solution(object):
    def pivotIndex(self, nums):
        total=sum(nums)
        for i in range(len(nums)):
            left=sum(nums[:i])
            right=total-left-nums[i]
            if left==right:
                return i
        return -1