class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        if len(bits)>2:
            for i in range(n-1):
                if len(bits)>2:
                    if bits[0]==1:
                        bits.remove(bits[0])
                        bits.remove(bits[0])
                    elif bits[0] == 0:
                        bits.remove(bits[0])
                print(bits)
        if len(bits)==1 and bits[0] == 0:
            return True
        elif bits ==[0,0]:
            return True

        return False