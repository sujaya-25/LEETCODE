class Solution(object):
    def scoreOfString(self, s):
        su=0
        for i in range(1,len(s)):
            diff=abs(ord(s[i])-ord(s[i-1]))
            su+=diff
        return su

        