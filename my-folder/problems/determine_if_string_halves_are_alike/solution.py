class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l = len(s)
        a=0
        vowels = "aeiouAEIOU"
        for i in s[:l//2]:
            if i in vowels:

                a+=1
        for i in s[(l//2):]:
            if i in vowels:
                a-=1
        return a==0

        