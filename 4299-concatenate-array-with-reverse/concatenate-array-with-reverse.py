class Solution(object):
    def concatWithReverse(self, nums):
        s=nums[::-1]
        nums.extend(s)
        return nums
        