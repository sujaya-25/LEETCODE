class Solution(object):
    def sortByBits(self, arr):
        a=[]
        b=[]
        for i in arr:
            c=bin(i)[2:].count("1")
            a.append([c,i])
        a.sort()
        for i in a:
            b.append(i[1])
        return b


        

        