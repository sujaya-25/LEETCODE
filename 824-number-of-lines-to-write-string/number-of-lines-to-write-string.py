class Solution(object):
    def numberOfLines(self,width,s):
        lines=1
        total=0

        for i in s:
            x=width[ord(i)-ord('a')]

            if total+x>100:
                lines+=1
                total=x
            else:
                total+=x

        return [lines,total]