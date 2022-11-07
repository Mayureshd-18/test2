from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = collections.Counter(nums1)
        c2 = collections.Counter(nums2)
        
        res = []
        for key in c1:
            if key in c2:
                res+= [key]*(min(c1[key],c2[key]))
        return res