class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        lst2 = map(str, digits)
        lst3 = []
        s = "".join(lst2)
        s2 = (int(s)+1)
        s3 = str(s2)
        for i in s3:
            lst3.append(int(i))

        return (lst3)