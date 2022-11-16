class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        lst = []
        while n >= 1:
            lst.append("0") if n % 2 == 0 else lst.append("1")
            n //= 2
        for i in range(len(lst)-1):
            if lst[i]==lst[i+1]:
                return False
        return True