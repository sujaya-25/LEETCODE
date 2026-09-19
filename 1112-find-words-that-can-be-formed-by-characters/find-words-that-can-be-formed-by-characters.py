class Solution(object):
    def countCharacters(self, words, chars):
        total=0
        
        for word in words:
            temp=chars
            ok=True
            
            for i in word:
                if i in temp:
                    temp=temp.replace(i,"",1)
                else:
                    ok=False
                    break
            
            if ok:
                total+=len(word)
        
        return total