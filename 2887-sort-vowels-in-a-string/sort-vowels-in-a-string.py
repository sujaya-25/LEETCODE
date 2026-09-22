class Solution(object):
    def sortVowels(self,s):
        v="aeiouAEIOU"
        a=[]
        
        for i in s:
            if i in v:
                a.append(i)
        
        a.sort()
        
        j=0
        b=""
        
        for i in s:
            if i in v:
                b+=a[j]
                j+=1
            else:
                b+=i
        
        return b