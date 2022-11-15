class Solution:
    def capitalizeTitle(self, title: str) -> str:
        res = []
        title = title.lower().split(" ")
        for i in title:
            if len(i)<3:
                res.append(i)
            else:
                res.append(i.title())
        return " ".join(res)