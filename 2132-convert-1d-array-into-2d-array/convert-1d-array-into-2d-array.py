
class Solution(object):
    def construct2DArray(self, original, m, n):
        if len(original) != m * n:
            return []
        
        a = []
        for i in range(0, len(original), n):
            a.append(original[i:i+n])
        
        return a
