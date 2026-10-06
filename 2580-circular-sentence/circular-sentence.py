class Solution(object):

    def isCircularSentence(self, sentence):

        s = sentence.split()
        f = True

        for i in range(len(s)):
            if s[i][-1] != s[(i+1) % len(s)][0]:
                f = False

        return f