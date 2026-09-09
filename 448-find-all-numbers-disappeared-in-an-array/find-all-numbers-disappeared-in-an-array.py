class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        s = set(nums)
        l = []
        for i in range(1, n + 1):
            if i not in s:
                l.append(i)
        return l