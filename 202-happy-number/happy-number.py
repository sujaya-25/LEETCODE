class Solution(object):
    def isHappy(self, n):
        seen=set()
        while n!=1:
            if n in seen:
                return False
            seen.add(n)
            ans=0
            while n>0:
                digit=n%10
                ans+=pow(digit,2)
                n=n//10
            n=ans
        return True