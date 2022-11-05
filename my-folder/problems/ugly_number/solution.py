class Solution:
    def isUgly(self, n: int) -> bool:
        pfact = []
        ugly = [2,3,5]
        if n<=0:
            return False
        while n % 2 == 0:
                pfact.append(2)
                n = n / 2

        for i in range(3,int(math.sqrt(n))+1,2):
    
            while n % i== 0:
                pfact.append(i)
                n = n / i

        if n > 2:
            pfact.append(n)
        print(pfact)
        for i in pfact:
            if i not in ugly:
                return False
        return True
    