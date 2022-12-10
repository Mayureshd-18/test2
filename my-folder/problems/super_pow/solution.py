class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        res = int("".join(map(str, b)))
        return pow(a,res,1337)
