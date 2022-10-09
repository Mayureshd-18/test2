class Solution:
    def isValid(self, s: str) -> bool:
        i= 0
        l = len(s)
        while(i<l):
            s=s.replace('()','')
            s=s.replace('[]','')
            s=s.replace('{}','')
            i+=1
        if(len(s)==0):
            return True
        else:
            return False
