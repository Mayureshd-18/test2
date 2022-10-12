class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        status = False
        nums.sort(reverse = True)

        while status != True:
            if (len(nums)==3) and (nums[1] + nums[2]<=nums[0]):
                return 0
            if nums[1] + nums[2]>nums[0] and len(nums)>=3:
                return sum(nums[:3])
            nums.remove(nums[0])
            
           