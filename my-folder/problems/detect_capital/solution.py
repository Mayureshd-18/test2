class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        first = word.lower()
        second = word.upper()
        third = word.title()
        return word in (first, second, third)