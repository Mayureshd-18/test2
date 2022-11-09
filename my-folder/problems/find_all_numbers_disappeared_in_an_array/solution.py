class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        occr = {}
        for i in range(1,len(nums)+1):
            occr[i] = 0
        for num in nums:
            occr[num] = 1
            
        l = []
        for key,value in occr.items():
            if value == 0:
                l.append(key)
        return l