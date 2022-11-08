class Solution:
    def makeGood(self, s: str) -> str:
        i=0
        s = list(s)
        while i < len(s)-1:
            if (s[i] == s[i+1].upper() or s[i].upper() == s[i+1]) and s[i] != s[i+1]:
                # print(s)
                s.pop(i)
                # print(s)
                s.pop(i)
                # print(s)
                i = -1
            i+=1
        result = ""
        for i in s:
            result += i
        return result