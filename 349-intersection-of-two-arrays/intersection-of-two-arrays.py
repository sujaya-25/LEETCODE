class Solution(object):
    def intersection(self, nums1, nums2):
        a=[]
        t=[]
        for i in nums1:
            if i in nums2:
                a.append(i)
        freq={}
        for k in a:
            if k in freq:
                freq[k]+=1
            else:
                freq[k]=1
        for key in freq:
            t.append(key)
        return t