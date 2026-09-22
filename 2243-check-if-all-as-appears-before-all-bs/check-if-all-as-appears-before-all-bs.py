class Solution(object):
    def checkString(self, s):
        seen_b = False
        for i in range(len(s)):
            if s[i] == "b":
                seen_b = True
            if s[i] == "a" and seen_b:
                return False
        return True