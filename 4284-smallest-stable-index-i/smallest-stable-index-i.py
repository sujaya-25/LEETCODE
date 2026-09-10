class Solution(object):
    def firstStableIndex(self, nums, k):
        n=len(nums)
        if n==1:
            return 0
        a=[]
        for i in range(n):
            m1=nums[0:i+1]
            m2=nums[i:n]
            diff=max(m1)-min(m2)
            if diff<=k:
                a.append(i)
        if a:
            return min(a)
        else:
            return -1


            
        