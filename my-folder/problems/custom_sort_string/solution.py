class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res = []
        for i in order:
            while i in s:
                res.append(i)
                s = s.replace(i,"",1)

        res .append(s)

        return("".join(res))
