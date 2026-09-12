class Solution(object):
    def countBinarySubstrings(self, s):
        a = []
        c = 1

        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                c += 1
            else:
                a.append(c)
                c = 1

        a.append(c)

        ans = 0
        for i in range(1, len(a)):
            ans += min(a[i], a[i-1])

        return ans