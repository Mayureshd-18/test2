class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        chars = {"color":1,"type":0,"name":2}
        count = 0
        for i in items:
            print(i[chars[ruleKey]])
            if i[chars[ruleKey]]== ruleValue:
                count+=1
                print(i)

        return count