class Solution:
    def reverseBits(self, n: int) -> int:
        string = format(n, 'b')
        string = '0' * (32-len(string)) +string
        string_new = '0b' + string[::-1] 
        return int(string_new, 2)