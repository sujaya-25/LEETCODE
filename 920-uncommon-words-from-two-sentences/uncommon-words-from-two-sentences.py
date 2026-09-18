class Solution(object):
    def uncommonFromSentences(self,s1,s2):
        a=(s1+" "+s2).split()
        freq={}

        for i in a:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1

        ans=[]

        for i in freq:
            if freq[i]==1:
                ans.append(i)

        return ans