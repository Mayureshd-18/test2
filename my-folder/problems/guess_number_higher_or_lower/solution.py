# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        max_val = n
        min_val = 1
        num = (n - 1)/2 + 1
        ans = guess(num)
        while ans != 0:
            if ans == -1:
                max_val = num - 1
            else:
                min_val = num + 1
            num = (max_val - min_val)/2 + min_val
            ans = guess(num)
        return int(num)
