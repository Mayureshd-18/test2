class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        occr = {}
        for i in nums:
            if i in occr:
                occr[i]+=1
            else:
                occr[i] = 1

        for i,j in occr.items():
            if j==1:
                return i