from math import sqrt
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = {2:True,3:True,5:True,7:True,11:True,13:True,17:True,19:True}
        res = 0
        for i in range(left,right+1):
            n = bin(i)[2:].count("1")
            if n in primes:
                res+=1

        return res
