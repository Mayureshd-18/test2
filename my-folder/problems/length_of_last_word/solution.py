class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lf = []
        s2 = s.strip()
        s2 = s2.split(" ")
        for i in s2:
            if len(i)>0:
                lf.append(i)
        return (len(lf[-1]))