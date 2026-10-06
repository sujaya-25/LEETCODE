class Solution(object):
    def countSeniors(self, details):
        a=[]
        c=0
        for i in details:
            a.append(i[11:13])
        for j in range(len(a)):
            if int(a[j])>60:
                c+=1
        return c

        