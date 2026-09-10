class Solution(object):
    def maximumWealth(self, accounts):
        mx=0
        s=0
        n=len(accounts)
        m=len(accounts[0])
        for i in range(n):
            s=sum(accounts[i])
            if mx<s:
                mx=s
        return mx
                
        