class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
            occr = {}
            for i in nums:
                occr[i] = occr.get(i,0)+1
            return [k for k,v in occr.items() if v == 1]
