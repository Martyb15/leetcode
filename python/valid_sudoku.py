class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row   = [set() for x in range(9)]
        col   = [set() for x in range(9)]
        boxes = [set() for x in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".": 
                    continue

                
                box_index = (i // 3) * 3 + (j // 3)

                if ( val in row[i] or val in col[j] or val in boxes[box_index]):
                    return False
                
                row[i].add(val)
                col[j].add(val)
                boxes[box_index].add(val)
        return True