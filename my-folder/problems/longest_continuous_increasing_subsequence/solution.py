class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        l = len(nums)
        if l==0:
            return 0
        ct = 1
        max = 0
        for i in range(l-1):
            if nums[i]<nums[i+1]:
                ct+=1
            else:
                if max<ct:
                    max = ct
                ct = 1
        
        if max<ct:
            max = ct
        return max