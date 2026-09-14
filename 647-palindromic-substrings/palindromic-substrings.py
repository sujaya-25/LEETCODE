class Solution(object):
    def countSubstrings(self, s):
        c = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                d = s[i:j+1]
                
                if d == d[::-1]:   
                    c += 1
        
        return c