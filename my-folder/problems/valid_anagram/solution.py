class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s2 = {}
        t2 = {}

        for i in s:
            s2[i] = s2.get(i,0)+1
        for j in t:
            t2[j] = t2.get(j,0)+1

        return s2==t2
