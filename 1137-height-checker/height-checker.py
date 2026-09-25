class Solution(object):
    def heightChecker(self, heights):
        l=len(heights)
        c=0
        exp=sorted(heights)
        for i in range(l):
            if heights[i]!=exp[i]:
                c+=1
        return c

        