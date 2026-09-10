class Solution(object):
    def numSpecial(self, mat):
        n=len(mat)
        m=len(mat[0])
        c=0
        for i in range(n):
            for j in range(m):
                if mat[i][j]==1:
                    s=0
                    for k in range(m):
                        if mat[i][k]==1:
                            s+=1
                    for k in range(n):
                        if mat[k][j]==1:
                            s+=1
                    if s==2:
                        c+=1
                    
        return c

        