class Solution(object):
    def reverseOnlyLetters(self, s):
        a = []
        for i in s:
            if i.isalpha():
                a.append(i)

        a.reverse()

        j = 0
        ans = ""
        for i in s:
            if i.isalpha():
                ans += a[j]
                j += 1
            else:
                ans += i

        return ans