class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        sentence = sentence.split(" ")
        res = ""
        vow =  ["a","e","o","u","i"]
        for i in range(len(sentence)):
            if sentence[i][0].lower() in vow:
                res += f"{sentence[i]}ma" + "a"*(i+1)
            else:
                res += sentence[i][1:]+sentence[i][0] + "ma" + ("a" * (i+1))
            res+= " "
        return res[:-1]