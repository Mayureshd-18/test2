class RandomizedCollection:

    def __init__(self):
        self.res = []

    def insert(self, val: int) -> bool:
        if val not in self.res:
            self.res.append(val)
            return True
        self.res.append(val)
        return False

    def remove(self, val: int) -> bool:
        try:
            self.res.remove(val)
            return True
        except:
            return False

    def getRandom(self) -> int:
         return random.choice(tuple(self.res))
        





# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()