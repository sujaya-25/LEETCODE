class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        a=[]
        for i in points:
            a.append(i[0])
        
        a.sort()
        
        ans=0
        for i in range(1,len(a)):
            ans=max(ans,a[i]-a[i-1])
        
        return ans