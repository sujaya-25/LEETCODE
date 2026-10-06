class Solution(object):
    def isAcronym(self, words, s):
        ans=""
        for i in range(len(words)):
            ans+=words[i][0]
        if ans==s:
            return True
        else:
            return False
        