class Solution(object):
    def toHex(self,num):
        if num==0:
            return "0"
        
        if num<0:
            num+=2**32
        
        a=""
        h="0123456789abcdef"
        
        while num>0:
            a=h[num%16]+a
            num=num//16
        
        return a