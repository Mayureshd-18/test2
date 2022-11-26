class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for i in ",.!?;'":
            paragraph = paragraph.replace(i, " ")
        paragraph = [str(word).lower() for word in paragraph.split()]

        occr = {}

        for i in paragraph:
            if i not in banned:
                occr[i] = occr.get(i,0) + 1

        return (max(occr, key = occr.get))
