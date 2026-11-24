import math
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        a=0
        for i in range(len(nums)):
            p=1
            g=0
            l=1
            for j in range(i,len(nums)):
                p*=nums[j]
                g=math.gcd(g,nums[j])
                l=math.lcm(l,nums[j])
                if p==g*l:
                    a=max(a,j-i+1)
        return a