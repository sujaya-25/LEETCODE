class Solution(object):
    def answerQueries(self, nums, queries):
        nums.sort()
        ans = []
        
        for q in queries:
            s = 0
            count = 0
            
            for num in nums:
                s += num
                if s <= q:
                    count += 1
                else:
                    break
            
            ans.append(count)
        
        return ans