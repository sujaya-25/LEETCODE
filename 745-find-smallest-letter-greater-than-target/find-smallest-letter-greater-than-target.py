class Solution(object):
    def nextGreatestLetter(self, letters, target):
        alpha="abcdefghijklmnopqrstuvwxyz"
        for i in range(len(alpha)):
            if alpha[i]>target and alpha[i] in letters:
                return alpha[i]
                
        return letters[0]
        