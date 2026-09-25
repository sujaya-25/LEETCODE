class Solution(object):
    def lastStoneWeight(self, stones):
        while len(stones)>1:
            stones.sort()
            frst=stones.pop()
            sec=stones.pop()
            if frst!=sec:
                stones.append(abs(sec-frst))
        if len(stones)==1:
            return stones[0]
        return 0

        