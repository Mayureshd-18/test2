class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        return [min(abs(j - i) for j in [i for i in range(len(s)) if s[i] == c]) for i in range(len(s))]
