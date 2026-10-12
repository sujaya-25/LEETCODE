class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        a = []
        for i in words:
            b = i.split(separator)
            for j in b:
                if j != "":
                    a.append(j)
        return a