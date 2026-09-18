class Solution(object):
    def diStringMatch(self,s):
        a=0
        b=len(s)
        ans=[]

        for i in s:
            if i=="I":
                ans.append(a)
                a+=1
            else:
                ans.append(b)
                b-=1

        ans.append(a)

        return ans