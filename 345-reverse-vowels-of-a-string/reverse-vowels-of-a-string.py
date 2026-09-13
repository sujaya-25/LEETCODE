class Solution(object):
    def reverseVowels(self,s):
        v="aeiouAEIOU"
        a=list(s)
        l=0
        r=len(a)-1

        while l<r:
            if a[l] not in v:
                l+=1
            elif a[r] not in v:
                r-=1
            else:
                a[l],a[r]=a[r],a[l]
                l+=1
                r-=1

        return "".join(a)