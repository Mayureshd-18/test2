class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ct = 0
        while val in nums:
            nums.remove(val)
            ct +=1
        print(ct,nums)