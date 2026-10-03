class Solution:
    def applyOperations(self, nums):
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0

        ans = []

        for x in nums:
            if x != 0:
                ans.append(x)

        while len(ans) < len(nums):
            ans.append(0)

        return ans