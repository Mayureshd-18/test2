class Solution:
    def search(self, list2: List[int], item: int) -> int:
        low = 0
        high = len(list2) - 1

        while low <= high:
            mid = int((low + high) / 2)
            # print(f"mid is {mid}")
            guess = list2[mid]
            # print(f"guess is {guess}")
            if guess == item:
                return mid
            elif guess > item:
                high = mid - 1
            else:
                low = mid + 1

        return -1
