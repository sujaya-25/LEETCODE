class Solution(object):
    def uniqueMorseRepresentations(self, words):
        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        a=set()
        
        for word in words:
            s=""
            for i in word:
                s+=morse[ord(i)-ord('a')]
            a.add(s)
        
        return len(a)