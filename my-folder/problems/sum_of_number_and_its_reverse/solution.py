class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        if num==0:
            return True
        status = False
        for i in range(num):
            i2 = str(i)
            i3 = i2[::-1]
            i4 = int(i3)
            if i + i4 == num:
                # print(f"{i} + {i4} ={n} ")
                status = True
                return status
            
        
        return status
                
            