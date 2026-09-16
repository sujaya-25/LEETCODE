class Solution(object):
    def convertToBase7(self,num):
        if num==0:
            return "0"
        
        sign=""
        if num<0:
            sign="-"
            num=-num
        
        s=""
        while num>0:
            r=num%7
            s=str(r)+s
            num=num//7
        
        return sign+s