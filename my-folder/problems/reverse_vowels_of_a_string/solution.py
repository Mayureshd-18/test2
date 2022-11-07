class Solution:
    def reverseVowels(self, s: str) -> str:
        lst = []
        s = list(s)
        vowels = ["a","e","i","o","u","A","E","I","O","U"]
        for i in s:
            if i in vowels:
                lst.append(i)

        print(lst)
        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = lst[-1]
                lst.pop()
        return ("".join(s))
