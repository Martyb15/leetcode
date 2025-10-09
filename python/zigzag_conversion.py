class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s
        
        direction = 1
        lists = [[] for i in range(numRows)]
        row = 0
        
        for i in s:
            lists[row].append(i)

            if row == 0:
                direction = 1
            elif row == numRows -1:
                direction = -1

            row += direction
        
                
        return "".join("".join(r) for r in lists )
        