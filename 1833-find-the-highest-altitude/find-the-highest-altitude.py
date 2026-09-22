class Solution(object):
    def largestAltitude(self, gain):
        s=[]
        s.append(0)
        for i in range(len(gain)):
            s.append(s[i]+gain[i])

        m=max(s)

        return m
        