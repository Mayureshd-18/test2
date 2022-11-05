class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occr = {}
        for i in nums:
            occr[i] = occr.get(i,0) + 1
        return max(occr,key = occr.get)