class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        even_occr = {}

        for i in nums:
            if i%2==0 : 
                if i not in even_occr:
                    even_occr[i] = 1
                else:
                    even_occr[i] +=1  

        if(len(even_occr))==0:
            return -1

        max_val = max(even_occr.values())
        ans = float('inf')
        for i,j in even_occr.items():
            if j==max_val:
                if i<ans:
                    ans = i

        
        return ans