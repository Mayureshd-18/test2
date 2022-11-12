class Solution:
    def findComplement(self, s: int) -> int:

        return int(bin(s)[2:].replace('1', 'temp').replace('0', '1').replace('temp', '0'),2)