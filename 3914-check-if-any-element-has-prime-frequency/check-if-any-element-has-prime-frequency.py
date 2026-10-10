
class Solution(object):
    def checkPrimeFrequency(self, nums):
        freq = {}

        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        for i in freq.values():
            if i > 1:
                prime = True

                for j in range(2, i):
                    if i % j == 0:
                        prime = False
                        break

                if prime:
                    return True

        return False
