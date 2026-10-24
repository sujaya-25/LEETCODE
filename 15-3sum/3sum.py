class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        a = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                s = nums[i] + nums[j] + nums[k]

                if s == 0:
                    a.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j-1]:
                        j += 1

                    while j < k and nums[k] == nums[k+1]:
                        k -= 1

                elif s < 0:
                    j += 1
                else:
                    k -= 1

        return a