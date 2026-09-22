class Solution(object):
    def sortSentence(self, s):
        t=s.split()
        b=[""]*len(t)
        for i in t:
            b[int(i[-1])-1]=i[:-1]
        return " ".join(b)
            

        