class Solution(object):
    def countEven(self, num):
        c = 0
        for i in range(1, num + 1):
            s = 0
            n = i   
            
            while n > 0:
                d = n % 10
                s = s + d
                n = n // 10

            if s % 2 == 0:
                c = c + 1
                
        return c