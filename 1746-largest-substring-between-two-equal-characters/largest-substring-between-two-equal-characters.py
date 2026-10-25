class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        a = {}
        ans = -1

        for i in range(len(s)):
            if s[i] in a:
                ans = max(ans, i - a[s[i]] - 1)
            else:
                a[s[i]] = i

        return ans