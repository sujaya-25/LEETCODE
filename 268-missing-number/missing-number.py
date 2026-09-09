class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        num=[]
        if n==1 and nums[0]==1:
            return 0
        elif n==1 and nums[0]==0:
            return 1
        else:
            for i in range(n+1):
                num.append(i)
            for k in num:
                if k not in nums:
                    return k
        

        