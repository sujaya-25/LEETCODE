class Solution(object):
    def subarraySum(self, nums, k):
        d={0:1}
        s=0
        c=0

        for x in nums:
            s=s+x

            if s-k in d:
                c=c+d[s-k]

            if s in d:
                d[s]=d[s]+1
            else:
                d[s]=1

        return c