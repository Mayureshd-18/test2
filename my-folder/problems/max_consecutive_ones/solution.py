class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len = 0
        temp = 0
        for i in nums:
            if i == 1:
                temp+=1

            else:
                if temp>max_len:
                    max_len=temp
                temp = 0

            if temp>max_len:
                max_len=temp

            print(temp)

        return max_len