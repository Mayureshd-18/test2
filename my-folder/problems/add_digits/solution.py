class Solution:
    def addDigits(self, n: int) -> int:
        while len(str(n))>1:
            n = str(n)
            sum = 0
            for i in range(len(n)):
                sum+= int(n[i])
            n = sum

        return n