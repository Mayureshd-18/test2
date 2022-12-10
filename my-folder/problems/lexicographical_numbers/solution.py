class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        strlst = [str(i) for i in range(1,n+1)]

        return list(map(int,sorted(strlst)))