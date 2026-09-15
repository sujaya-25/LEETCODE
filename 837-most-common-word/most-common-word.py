class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        paragraph=paragraph.lower()

        for x in "!?',;.":
            paragraph=paragraph.replace(x," ")

        words=paragraph.split()

        freq={}

        for i in words:
            if i not in banned:
                if i not in freq:
                    freq[i]=1
                else:
                    freq[i]+=1

        m=0
        ans=""

        for key in freq:
            if freq[key]>m:
                m=freq[key]
                ans=key

        return ans