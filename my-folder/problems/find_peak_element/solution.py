class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums2 = nums[:]

        return nums.index(sorted(nums2)[-1])