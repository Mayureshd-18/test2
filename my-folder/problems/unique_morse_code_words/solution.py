class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..",'j':".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--",'z':"--.."}
        res = set()
        for i in words:
            temp = []
            for j in i:
                temp.append(morse[j])
            s = "".join(temp)

            res.add(s)

        return len(res)