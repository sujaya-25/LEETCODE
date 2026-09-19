class Solution(object):
    def commonChars(self, words):
        a=[]
        
        for i in words[0]:
            if all(i in j for j in words):
                a.append(i)
                words=[j.replace(i,"",1) for j in words]
        
        return a