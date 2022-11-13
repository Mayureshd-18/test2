class Solution:
    def convertToBase7(self, num: int) -> str:
        if num==0:
            return "0"
        res = []
        flag = 0
        if num<0:
            num*=-1
            flag = 1
        while num>0:
            res.append(num%7)
            num//=7

        res = list(map(str,res))

        if flag ==0:
            return  "".join(res[::-1])
        else:
            return "-"+"".join(res[::-1])