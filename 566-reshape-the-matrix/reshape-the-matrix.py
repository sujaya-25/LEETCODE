class Solution:
    def matrixReshape(self, mat, r, c):
        if len(mat)*len(mat[0])!=r*c:
            return mat
        
        a=[]
        for row in mat:
            for x in row:
                a.append(x)
        
        ans=[]
        k=0
        
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(a[k])
                k+=1
            ans.append(row)
        
        return ans