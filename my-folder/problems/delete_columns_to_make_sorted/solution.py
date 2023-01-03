class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])
        ct = 0
        for i in range(n):
            status = 0
            for j in range(len(strs)-1):
                # print(strs[j][i],strs[j+1][i])
                if not status and ord(strs[j + 1][i]) < ord(strs[j][i]) :
                    ct+=1
                    status = 1
                    # print("non lexo are",strs[j][i],strs[j+1][i])



        return (ct)