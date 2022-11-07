class Solution:
    def sortSentence(self, s: str) -> str:
        
        spl = s.split(" ")
        
        srt = sorted(spl, key=lambda w: w[-1])
        print(srt)
        word = [w[:-1] for w in srt]
        print(word)
        return " ".join(word)
