class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        occr = {}
        for i in candyType:
            occr[i] = occr.get(i,0)+1
        n = len(candyType)
        if len(occr)>n/2:
            return n//2
        return len(occr)