class Solution(object):
    def findRestaurant(self, list1, list2):
        m=float("inf")
        ans=[]
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    s=i+j
                    if s<m:
                        m=s
                        ans=[list1[i]]
                    elif s==m:
                        ans.append(list1[i])
        return ans
