class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        ns = ''.join(S.split("-")).upper()
        n = len(ns)
        res = []
            
        if n % K != 0:
            res.append(ns[:n % K])
        for i in range(n % K, len(ns), K):
            res.append(ns[i:i + K ])
        return '-'.join(res)