class Solution:
    def mergeSimilarItems(self, items1, items2):
        d = {}

        for x, y in items1:
            d[x] = y

        for x, y in items2:
            d[x] = d.get(x, 0) + y

        return sorted([[x, y] for x, y in d.items()])