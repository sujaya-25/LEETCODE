class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        a=[]
        for i in range(len(nums)):
            left=sum(nums[:i])
            right=sum(nums[i+1:])
            a.append(abs(left-right))
        return a