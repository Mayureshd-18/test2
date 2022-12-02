class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
           
        comb = []
        for i in range(len(nums)+1):
            # for j in combinations(nums,i):
            #     if 
            #     
            for j in combinations(nums, i):
                if sorted(list(j)) not in comb:
                    comb.append(sorted(list(j)))
            # comb += [if list(j) not in comb: list(j)  ]
        return comb