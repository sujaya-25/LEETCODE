class Solution(object):
    def findComplement(self, num):
        a=[]
        ans=""
        bina=bin(num)[2:]
        for i in range(len(bina)):
            if bina[i]=='0':
                ans+='1'
            else:
                ans+='0'
        return int(ans,2)
        