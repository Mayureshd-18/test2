class Solution:
    def findMin(self, nums: List[int]) -> int:
        return (reduce(min,nums) )