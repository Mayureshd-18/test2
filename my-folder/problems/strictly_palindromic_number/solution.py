import string
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        

        status = True
        
        
        
        def to_base(value, base, digits=string.digits + string.ascii_letters):  

            digits_slice = digits[0:base]

            temporary_var = value
            data = [temporary_var]

            while True:
                temporary_var = temporary_var // base
                data.append(temporary_var)
                if temporary_var < base:
                    break

            result = ''
            for each_data in data:
                result += digits_slice[each_data % base]
            result = result[::-1]

            return result
        
        for i in range(2,n+1):
            x = to_base(n, base = i)
            if x == x[::-1]:
                status = True
            else:
                status = False
                break
            # print(i,to_base(n, base = i))

        return status

       
