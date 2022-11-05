class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        occr = {}
        for i in nums:
            occr[i] = occr.get(i,0)+1
        return min(occr,key = occr.get)