class Solution:
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        a=[]
        
        for i in range(rows):
            for j in range(cols):
                d=abs(i-rCenter)+abs(j-cCenter)
                a.append([d,i,j])
        
        a.sort()
        
        ans=[]
        for x in a:
            ans.append([x[1],x[2]])
        
        return ans