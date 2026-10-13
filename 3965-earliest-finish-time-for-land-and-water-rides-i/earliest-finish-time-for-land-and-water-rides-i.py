
class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        ans = float('inf')

        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                a = max(landStartTime[i] + landDuration[i], waterStartTime[j]) + waterDuration[j]
                b = max(waterStartTime[j] + waterDuration[j], landStartTime[i]) + landDuration[i]

                ans = min(ans, a, b)

        return ans
