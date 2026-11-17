class Solution:
    def convertDateToBinary(self, date: str) -> str:
        a=date.split("-")
        b=[]
        for i in a:
            b.append(bin(int(i))[2:])
        return "-".join(b)