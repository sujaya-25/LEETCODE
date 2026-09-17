class Solution(object):
    def shortestToChar(self,s,c):
        ans=[]

        for i in range(len(s)):
            m=len(s)

            for j in range(len(s)):
                if s[j]==c:
                    m=min(m,abs(i-j))

            ans.append(m)

        return ans