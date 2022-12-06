class Solution:
    def hIndex(self, citations: List[int]) -> int:
        length=len(citations)
        i=0
        while i<length:
            if citations[i]>=len(citations)-i:
                return len(citations)-i
            i+=1
        return 0