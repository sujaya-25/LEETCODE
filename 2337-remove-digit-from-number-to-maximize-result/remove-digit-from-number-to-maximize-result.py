class Solution(object):
    def removeDigit(self,number,digit):
        ans=""
        
        for i in range(len(number)):
            if number[i]==digit:
                a=number[:i]+number[i+1:]
                if a>ans:
                    ans=a
        
        return ans