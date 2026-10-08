class Solution(object):
    def maxFreqSum(self, s):
        v="aeiou"
        freq={}
        a=[]
        b=[]
        for i in s:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        for key in freq:
            if key in v:
                a.append(freq[key])
            else:
                b.append(freq[key])
        x=0
        y=0
        if a:
            x=max(a)
        if b:
            y=max(b)
        return x+y
    
            
        