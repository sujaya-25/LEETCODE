class Solution(object):
    def lengthOfLongestSubstring(self, s):
        c=set()
        m=0
        l=0
        for r in range(len(s)):
            while s[r] in c:
                c.remove(s[l])
                l=l+1

            c.add(s[r])
            m=max(m,r-l+1)

        return m
    

        