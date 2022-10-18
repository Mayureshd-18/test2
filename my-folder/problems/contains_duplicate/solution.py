class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = dict()
        
        for index in range(len(nums)):
            if nums[index] in seen:
                return True
            else:
                seen[nums[index]] = index
            
        return False