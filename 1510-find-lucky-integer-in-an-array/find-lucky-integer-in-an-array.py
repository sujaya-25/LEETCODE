class Solution(object):
    def findLucky(self, arr):
        freq={}
        a=[]
        for i in arr:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        for key in freq:
            if freq[key]==key:
                a.append(key)
        if a:
            return max(a)
        else:
            return -1
        