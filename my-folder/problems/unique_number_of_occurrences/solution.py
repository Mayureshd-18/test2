class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occr = {}
        for i in arr:
            occr[i] = occr.get(i,0)+1
        occrofoccr = {}
        for i in occr.values():
            if i in occrofoccr:
                return False
            occrofoccr[i] = 1
        return True
