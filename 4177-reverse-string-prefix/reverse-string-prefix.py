class Solution(object):
    def reversePrefix(self, s, k):
        ans=""
        ans+=s[:k][::-1]+s[k:]
        return ans
        

        