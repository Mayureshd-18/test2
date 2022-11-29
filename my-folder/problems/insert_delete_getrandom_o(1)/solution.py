import random
class RandomizedSet:

    def __init__(self):
        self.res = set()
        
    def insert(self, val: int) -> bool:
        if val not in self.res:
            self.res.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        try:
            self.res.remove(val)
            return True
        except:
            return False

    def getRandom(self) -> int:
        return random.choice(tuple(self.res))



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()