class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        a=[]
        b=[]
        for i in range(len(arr2)):
            for j in range(arr1.count(arr2[i])):
                a.append(arr2[i])
        for i in range(len(arr1)):
            if arr1[i] not in arr2:
                b.append(arr1[i])
        b.sort()
        a.extend(b)
        return a