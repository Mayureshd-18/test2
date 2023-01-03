class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        for i in nums:
            if i>0:
                pos.append(i)
            else:
                neg.append(i)

        res = []
        for i in range(len(pos)):
            res.extend((pos[i], neg[i]))
        
        return res