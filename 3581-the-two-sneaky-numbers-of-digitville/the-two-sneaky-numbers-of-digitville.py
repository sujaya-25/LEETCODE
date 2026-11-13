class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        a=[]
        for i in nums:
            if nums.count(i)>1 and i not in a:
                a.append(i)
        return a