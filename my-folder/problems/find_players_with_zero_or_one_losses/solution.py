class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win,lose = {},{}

        for i in matches:
            win[i[0]] = win.get(i[0],0)+1
            lose[i[1]] = lose.get(i[1],0)+1

        res1 = [i for i in win if i not in lose]
        res2 = [i for i, j in lose.items() if j==1]
        res = [sorted(res1),sorted(res2)]

        return(res)