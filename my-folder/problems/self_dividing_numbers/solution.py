class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        import contextlib

        res = []
        for i in range(left,right+1):
            with contextlib.suppress(ZeroDivisionError):
                s = str(i)
                stat = all(i%int(j) == 0 for j in s)
                if stat:
                    res.append(i)
        return res
