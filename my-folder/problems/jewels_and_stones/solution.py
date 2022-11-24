class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        char = list(set(J))
        _list = []
        for c in char:
            _list.append(S.count(c))
        return sum(_list)

        