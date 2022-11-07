class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict_ = {}
        for i in s:
            dict_[i] = dict_.get(i,0)+1
        for x,y in dict_.items():
            if y==1:
                return s.index(x)
        return -1