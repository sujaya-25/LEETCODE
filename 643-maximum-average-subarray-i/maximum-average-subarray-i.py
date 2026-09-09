class Solution(object):
    def findMaxAverage(self, nums, k):
        s = sum(nums[:k])
        m = s

        for i in range(k, len(nums)):
            s += nums[i]
            s -= nums[i-k]

            if s > m:
                m = s

        return float(m) / k