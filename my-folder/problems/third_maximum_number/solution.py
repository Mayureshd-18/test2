class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        occr = {}
        for i in nums:
            occr[i] = occr.get(i,0)+1

        occr = sorted(occr.keys(),reverse = True)

        if len(occr)>2:
            return occr[2]
        
        return occr[0]