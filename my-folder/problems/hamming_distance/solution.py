class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = bin(x)[2:]
        y = bin(y)[2:]
        ml = max(len(x),len(y))
        x = x.zfill(ml)
        y = y.zfill(ml)
        ct = 0
        for i in range(len(x)):
            if x[i]!=y[i]:
                ct+=1

        return ct
