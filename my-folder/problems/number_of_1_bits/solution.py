class Solution:
    def hammingWeight(self, n: int) -> int:
        n1 = bin(n)
        return n1.count("1")