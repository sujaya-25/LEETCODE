class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ev=[]
        od=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                ev.append(nums[i])
            else:
                od.append(nums[i])
        ev.extend(od)
        return ev
        
        