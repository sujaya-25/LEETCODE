class Solution(object):
    def addBinary(self, a, b):
        ab=int(a,2)
        bb=int(b,2)
        sums=ab+bb
        binary=bin(sums)[2:]
        return binary
        