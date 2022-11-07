class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        num = 0
        s = s.split(" ")
        for i in s:
            if i.isnumeric():
                if int(i)<=num:
                    return False
                num = int(i)

        return True
