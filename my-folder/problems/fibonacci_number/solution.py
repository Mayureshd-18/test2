class Solution:
    def fib(self, n: int) -> int:
        return int((((1+sqrt(5))**n)-((1-sqrt(5)))**n)/(2**n*sqrt(5)))