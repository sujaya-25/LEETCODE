class Solution:
    def findEvenNumbers(self, digits):
        count = [0] * 10

        for d in digits:
            count[d] += 1

        ans = []

        for num in range(100, 1000, 2):
            temp = num
            need = [0] * 10

            while temp > 0:
                need[temp % 10] += 1
                temp //= 10

            ok = True

            for i in range(10):
                if need[i] > count[i]:
                    ok = False
                    break

            if ok:
                ans.append(num)

        return ans