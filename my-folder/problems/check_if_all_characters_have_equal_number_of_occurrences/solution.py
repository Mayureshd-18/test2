class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        occr = {}
        for i in s:
            occr[i] = occr.get(i,0) + 1

        return len(set(occr.values()))==1