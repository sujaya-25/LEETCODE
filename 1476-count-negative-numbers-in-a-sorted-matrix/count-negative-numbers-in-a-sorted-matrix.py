class Solution(object):
    def countNegatives(self, grid):
        r=len(grid)
        col=len(grid[0])
        c=0
        for i in range(r):
            for j in range(col):
                if grid[i][j]<0:
                    c=c+1

        return c