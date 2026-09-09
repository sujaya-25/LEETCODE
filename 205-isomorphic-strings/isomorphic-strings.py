class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s)!=len(t):
            return False
        a=[]
        b=[]
        for i in range(len(s)):
            if s[i] not in a:
                a.append(s[i])
            if t[i] not in b:
                b.append(t[i])

        for j in range(len(s)):
            if a.index(s[j])!=b.index(t[j]):
                return False
        return True

        