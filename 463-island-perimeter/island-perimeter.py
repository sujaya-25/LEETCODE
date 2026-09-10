class Solution(object):
    def islandPerimeter(self, grid):
        n=len(grid)
        m=len(grid[0])
        c=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    s=4
                    if i>0 and grid[i-1][j]==1:
                        s-=1
                    if i<n-1 and grid[i+1][j]==1:
                        s-=1
                    if j>0 and grid[i][j-1]:
                        s-=1
                    if j<m-1 and grid[i][j+1]==1:
                        s-=1
                    c+=s
        return c
        