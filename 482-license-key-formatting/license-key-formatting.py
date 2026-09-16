class Solution(object):
    def licenseKeyFormatting(self,s,k):
        s=s.replace("-","").upper()
        a=[]
        
        first=len(s)%k
        if first:
            a.append(s[:first])
        
        for i in range(first,len(s),k):
            a.append(s[i:i+k])
        
        return "-".join(a)