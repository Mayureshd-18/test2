import random
class Solution:

    def __init__(self, nums: List[int]):
        self.lst = nums
        self.copy = self.lst.copy()

    def reset(self) -> List[int]:

        return self.copy

    def shuffle(self) -> List[int]:
        random.shuffle(self.lst)
        return self.lst


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()