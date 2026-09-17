class Solution(object):
    def toGoatLatin(self,s):
        a=s.split()
        ans=[]
        x="a"

        for word in a:
            if word[0].lower() in "aeiou":
                word=word+"ma"+x
            else:
                word=word[1:]+word[0]+"ma"+x

            ans.append(word)
            x+="a"

        return " ".join(ans)