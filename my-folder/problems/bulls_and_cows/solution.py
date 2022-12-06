class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = sum(a==b for a,b in zip(secret, guess))
        cows = collections.Counter(secret) & collections.Counter(guess)
        return(f"{bulls}A{sum(cows.values()) - bulls}B")

