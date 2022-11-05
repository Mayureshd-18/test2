class Solution:
    def isHappy(self, n: int) -> bool:
        visited = []
        while n != 1:
            sum = 0
            n = str(n)
            for i in range(len(n)):
                sum+= int(n[i])**2
            n = sum
            if n not in visited:
                visited.append(n)
                print(n, visited)
            else:
                print("Chakwa basla")
                return False
        return True
