class Solution(object):
    def findRotation(self, mat, target):
        for k in range(4):
            if mat == target:
                return True

            mat = [list(row) for row in zip(*mat[::-1])]

        return False