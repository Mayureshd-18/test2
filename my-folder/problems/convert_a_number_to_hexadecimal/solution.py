class Solution:
    def toHex(self, num: int) -> str:
        m = dict.fromkeys(range(16), 0)
    
        digit = ord('0')
        c = ord('a')
    
        for i in range(16) :
            if (i < 10) :
                m[i] = chr(digit)
                digit += 1
            
            else :
                m[i] = chr(c)
                c += 1

        res = ""

        if (not num) :
            return "0"

        if (num > 0) :
            while (num) :
                res = m[num % 16] + res
                num //= 16

        else :

            n = num + 2**32
    

            while (n) :
                res = m[n % 16] + res
                n //= 16
    
        return res