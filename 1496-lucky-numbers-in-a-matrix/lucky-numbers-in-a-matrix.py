class Solution(object):
    def luckyNumbers(self, matrix):
        n=len(matrix)
        m=len(matrix[0])
        res=[]
        for i in range(n):
            x=min(matrix[i])
            for j in range(m):
                if matrix[i][j]==x:
                    c=0
                    for k in range(n):
                        if matrix[k][j]>x:
                            c=1
                    if c==0:
                        res.append(x)
        return res



            

        