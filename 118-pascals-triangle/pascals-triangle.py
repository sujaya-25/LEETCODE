class Solution(object):
    def generate(self, numRows):
        numrows=[]
        for i in range(numRows):
            row=[1]*(i+1)
            for j in range(1,i):
                row[j]=numrows[i-1][j-1]+numrows[i-1][j]
            numrows.append(row)
        return numrows


        