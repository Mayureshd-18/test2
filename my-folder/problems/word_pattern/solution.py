class Solution:
    def wordPattern(self, s: str, t: str) -> bool:
        if s == t == "":
            return True
        t = t.split(" ")
        if len(s)!=len(t):
            return False
        compare = {}
        for i in range(len(s)):
            if s[i] not in compare: 
                if t[i] in compare.values():
                    return False
                compare[s[i]] = t[i]
            else:
                if compare[s[i]] != t[i]:
                    return False
       
        return True