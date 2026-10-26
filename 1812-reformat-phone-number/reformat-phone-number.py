class Solution(object):
    def reformatNumber(self, number):
        s = ""

        for i in number:
            if i.isdigit():
                s += i

        res = []
        i = 0

        while len(s) - i > 4:
            res.append(s[i:i+3])
            i += 3

        if len(s) - i == 4:
            res.append(s[i:i+2])
            res.append(s[i+2:i+4])
        else:
            res.append(s[i:])

        return "-".join(res)