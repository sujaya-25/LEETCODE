class Solution(object):
    def removeOuterParentheses(self, s):
        a=""
        count=0
        
        for i in s:
            if i=="(":
                if count>0:
                    a+=i
                count+=1
            else:
                count-=1
                if count>0:
                    a+=i
        
        return a