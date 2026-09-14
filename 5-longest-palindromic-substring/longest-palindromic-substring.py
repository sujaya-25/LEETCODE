class Solution(object):
    def longestPalindrome(self, s):
        res = ""
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                e = s[i:j+1]
                
                if e == e[::-1] and len(e) > len(res):
                    res = e
                    
        return res