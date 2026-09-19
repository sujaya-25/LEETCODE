class Solution(object):
    def freqAlphabets(self,s):
        a=""
        i=0
        
        while i<len(s):
            if i+2<len(s) and s[i+2]=="#":
                n=int(s[i:i+2])
                i+=3
            else:
                n=int(s[i])
                i+=1
            
            a+=chr(ord('a')+n-1)
        
        return a