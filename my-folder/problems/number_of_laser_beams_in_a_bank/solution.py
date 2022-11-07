class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        dev = []
        num = 0
        for i in bank:
            dev.append(i.count("1"))
        while 0 in dev:
            dev.remove(0)
        print(dev)
        for i in range(len(dev)-1):
            num+=dev[i]*dev[(i+1)]
        return (num)