from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        
        s_ = Counter(s)
        t_ = Counter(t)
        
        return list(t_ - s_)[0]