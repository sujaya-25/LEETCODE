class Solution(object):
    def destCity(self, paths):
        start=[]
        
        for i in paths:
            start.append(i[0])
        
        for i in paths:
            if i[1] not in start:
                return i[1]