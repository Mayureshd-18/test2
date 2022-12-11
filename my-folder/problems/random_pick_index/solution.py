class Solution:

    def __init__(self, nums: List[int]):
        self.hashmap = defaultdict(list)
        for idx, num in enumerate(nums):
            self.hashmap[num].append(idx)

    def pick(self, target: int) -> int:
        return self.hashmap[target][random.randint(0,len(self.hashmap[target])-1)]