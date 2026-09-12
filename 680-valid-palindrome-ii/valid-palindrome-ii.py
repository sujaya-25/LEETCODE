class Solution(object):
    def validPalindrome(self, s):
        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] != s[j]:
                a = s[i+1:j+1]
                b = s[i:j]
                return a == a[::-1] or b == b[::-1]

            i += 1
            j -= 1

        return True