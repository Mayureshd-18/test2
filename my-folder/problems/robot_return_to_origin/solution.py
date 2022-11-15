class Solution:
    def judgeCircle(self, moves: str) -> bool:
        occr = {"U":0,"D":0,"L":0,"R":0}
        for i in moves:
                occr[i]+=1
        return occr["U"]==occr["D"] and occr["L"]==occr["R"]
        return False