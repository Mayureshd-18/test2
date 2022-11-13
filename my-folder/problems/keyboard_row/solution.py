class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        res=[]
        top_row=set('qwertyuiop')
        mid_row=set('asdfghjkl')
        bottom_row=set('zxcvbnm')
        for word in words:
            if set(word.lower()).issubset(top_row) or set(word.lower()).issubset(mid_row) or set(word.lower()).issubset(bottom_row):
                res.append(word)
        return res
