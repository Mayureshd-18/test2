class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        nums2 = list(map(str,nums))
        list2 = []
        for i in nums2:
            list2.append(i[::-1])
        list2 = list(map(int,list2))
        # print(list2)
        listf = nums + list2
        return (len(set(listf)))