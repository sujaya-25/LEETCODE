class Solution(object):
    def longestPalindrome(self, s):
        d = {}
        for i in s:
            d[i] = d.get(i, 0) + 1

        ans = 0
        odd = 0

        for i in d:
            if d[i] % 2 == 0:
                ans += d[i]
            else:
                ans += d[i] - 1
                odd = 1

        return ans + odd