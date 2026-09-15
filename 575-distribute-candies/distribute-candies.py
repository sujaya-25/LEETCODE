class Solution(object):
    def distributeCandies(self, candyType):
        n=len(candyType)
        c=0
        freq={}
        for i in candyType:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        for key in freq:
            c+=1
        return min(c,n//2)