class Solution(object):
    def isSameAfterReversals(self, num):
        original = num
        
        r = 0
        while num > 0:
            d = num % 10
            r = r * 10 + d
            num = num // 10
        
        t = 0
        while r > 0:
            f = r % 10
            t = t * 10 + f
            r = r // 10
        
        return original == t