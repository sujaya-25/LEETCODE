class Solution(object):
    def trailingZeroes(self,n):
        c=0
        while n>=5:
            n=n//5
            c+=n
        return c