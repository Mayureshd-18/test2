class Solution:
    def reverse(self, x: int) -> int:
        n1 = -2**31
        n2 = (2**31)-1
        x2 = str(x)
        if x2[0] == "-":
            x3 = x2[1:]
            x4 = f"-{x3[::-1]}"
        else:
            x4 = x2[::-1]
            
        if n1<=int(x4)<=n2:
            return int((x4))
        else:
            return 0