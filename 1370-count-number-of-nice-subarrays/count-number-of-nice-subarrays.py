class Solution(object):
    def numberOfSubarrays(self, nums, k):
        d={0:1}
        c=0
        odd=0

        for x in nums:
            if x%2!=0:
                odd=odd+1

            if odd-k in d:
                c=c+d[odd-k]

            if odd in d:
                d[odd]=d[odd]+1
            else:
                d[odd]=1

        return c