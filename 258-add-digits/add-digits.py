class Solution(object):
    def addDigits(self, num):
        while num>=10:
            s=0
            while num>0:
                digit=num%10
                num=num//10
                s+=digit
            num=s
        return num
        