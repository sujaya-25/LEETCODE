class Solution(object):
    def subarraysDivByK(self, nums, k):
        d={0:1}
        s=0
        c=0

        for x in nums:
            s=s+x
            r=s%k

            if r in d:
                c=c+d[r]
            else:
                d[r]=0

            d[r]=d[r]+1

        return c