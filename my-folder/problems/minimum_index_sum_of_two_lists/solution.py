class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        set1 = list(set(list1) & set(list2))
        min_index = [list2.index(i)+list1.index(i) for i in set1]
        mini = min(min_index)
        return [set1[i] for i in range(len(min_index)) if min_index[i]==mini]