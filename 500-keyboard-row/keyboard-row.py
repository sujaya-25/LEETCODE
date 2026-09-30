class Solution:
    def findWords(self, words):
        rows=["qwertyuiop","asdfghjkl","zxcvbnm"]
        ans=[]
        
        for word in words:
            w=word.lower()
            
            for row in rows:
                if all(ch in row for ch in w):
                    ans.append(word)
                    break
        
        return ans