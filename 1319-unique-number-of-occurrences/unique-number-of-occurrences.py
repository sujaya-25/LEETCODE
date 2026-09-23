class Solution:
    def uniqueOccurrences(self, arr):
        a=[]
        
        for x in arr:
            if x not in a:
                a.append(x)
        
        b=[]
        for x in a:
            b.append(arr.count(x))
        
        return len(b)==len(set(b))