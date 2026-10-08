class Solution(object):
    def passwordStrength(self, password):
        s=set(password)
        #l=list(s)
        c=0
        v="!@#$%^&*()"
        for i in s:
            if 'a'<=i<='z':
                c+=1
            if 'A'<=i<='Z':
                c+=2
            if '0'<=i<='9':
                c+=3
            if i in v:
                c+=5
        return c
        