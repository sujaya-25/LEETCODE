class Solution(object):
    def minOperations(self, logs):
        a=0
        
        for i in logs:
            if i=="../":
                if a>0:
                    a-=1
            elif i=="./":
                continue
            else:
                a+=1
        
        return a