class Solution(object):
    def isPathCrossing(self, path):
        x=0
        y=0
        seen={(0,0)}
        
        for i in path:
            if i=="N":
                y+=1
            elif i=="S":
                y-=1
            elif i=="E":
                x+=1
            else:
                x-=1
            
            if (x,y) in seen:
                return True
            
            seen.add((x,y))
        
        return False