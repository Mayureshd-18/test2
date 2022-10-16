class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        status = False
        pos = []
        neg = []
        for i in nums:
            if i>0:
                pos.append(i)
            else:
                neg.append(i)
                
        pos.sort(reverse = True)
        neg.sort()
        
        for j in pos:
            if j*-1 in neg:
                return j
                status = True
                break
                
                
        if status ==False:
            return -1
            