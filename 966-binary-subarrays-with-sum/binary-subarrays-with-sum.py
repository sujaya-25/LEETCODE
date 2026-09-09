class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        d={0:1}
        s=0
        c=0

        for x in nums:
            s=s+x

            if s-goal in d:
                c=c+d[s-goal]

            if s in d:
                d[s]=d[s]+1
            else:
                d[s]=1

        return c