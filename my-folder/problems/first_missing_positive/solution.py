class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        for i in nums:
            if i<=0:
                nums.remove(i)

        i = 1
        for j in nums:
            if i==j:
                i+=1



        return i