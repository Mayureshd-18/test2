class Solution:
    def maximum69Number (self, n: int) -> int:
        n2 = list(str(n))
        for i in range(len(n2)):
            if n2[i] == "6":
                n2[i] = "9"
                break
        res = "".join(n2)
        return (res)