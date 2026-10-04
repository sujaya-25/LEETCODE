class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        ans = 0

        for i in range(len(hours)):
            if hours[i] >= target:
                ans += 1

        return ans