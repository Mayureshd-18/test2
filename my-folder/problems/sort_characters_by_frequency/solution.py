class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        s2 = ""
        for i in s:
            d[i] = d.get(i,0)+1
        for w in sorted(d, key=d.get, reverse=True):
            s2 += (w*d[w])

        return s2