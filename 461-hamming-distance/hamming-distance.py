class Solution(object):
    def hammingDistance(self, x, y):
        n = x ^ y
        c = 0
        while n > 0:
            if n % 2 == 1:
                c += 1
            n = n // 2
        return c