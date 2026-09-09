class Solution(object):
    def backspaceCompare(self, s, t):
        a = []
        b = []
        for x in s:
            if x == '#':
                if a:
                    a.pop()
            else:
                a.append(x)
        for x in t:
            if x == '#':
                if b:
                    b.pop()
            else:
                b.append(x)
        return a == b