class Solution:
    def printVertically(self, s: str) -> List[str]:
        A, S = [], s.split()
        M  = max(map(len,S))
        for i in range(M):
            c = ''
            for s in S: c += ' ' if i >= len(s) else s[i]
            A.append(c.rstrip())
        return A