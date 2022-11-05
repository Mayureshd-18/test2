class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        for j in nums:
            if i==j:
                i+=1

        return i