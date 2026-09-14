class Solution(object):
    def convertToTitle(self,columnNumber):
        s=""
        
        while columnNumber>0:
            columnNumber-=1
            s=chr(columnNumber%26+65)+s
            columnNumber//=26
        
        return s