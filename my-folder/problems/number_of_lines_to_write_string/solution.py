class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        ABC = "abcdefghijklmnopqrstuvwxyz"
        counter, lines = 0, 1 
        _dict = {}
                
        for i in range(len(widths)):
            _dict[ABC[i]] = widths[i]
        for i in S:
            counter += _dict[i]
            if counter > 100:
                lines += 1
                counter = _dict[i]
                
        return [lines, counter]