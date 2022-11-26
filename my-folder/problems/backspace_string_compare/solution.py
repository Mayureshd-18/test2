
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sstack = []
        tstack = []

        for i in s:
            if i=="#":
                if sstack!=[]:
                    sstack.pop()
            else:
                sstack.append(i)

        for j in t:
            if j=="#":
                if tstack!=[]:
                    tstack.pop()
            else:
                tstack.append(j)
        return (sstack==tstack)

