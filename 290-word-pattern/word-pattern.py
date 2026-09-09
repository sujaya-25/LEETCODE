class Solution(object):
    def wordPattern(self, pattern, s):
        t=s.split()
        if len(pattern)!=len(t):
            return False
        a=[]
        b=[]
        for i in range(len(pattern)):
            if pattern[i] not in a:
                a.append(pattern[i])
            if t[i] not in b:
                b.append(t[i])

        for k in range(len(pattern)):
            if a.index(pattern[k])!=b.index(t[k]):
                return False
        return True
        