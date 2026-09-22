class Solution(object):
    def sortPeople(self,names,heights):
        a=[]
        
        for i in range(len(names)):
            a.append([heights[i],names[i]])
        
        a.sort(reverse=True)
        
        b=[]
        
        for i in a:
            b.append(i[1])
        
        return b