class Solution(object):
    def vowelStrings(self, words, left, right):
        c=0
        v="AEIOUaeiuo"
        for i in range(left,right+1):
            if words[i][0] in v and words[i][-1] in v:
                c+=1
        return c
        