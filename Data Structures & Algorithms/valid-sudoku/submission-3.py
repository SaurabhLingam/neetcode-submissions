class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val == ".": continue
                if val in rows[i]: return False
                elif val in cols[j]: return False
                elif val in box[((i//3) * 3) + (j//3)]: return False
                else:
                    rows[i].add(val)
                    cols[j].add(val)
                    box[((i//3) * 3) + (j//3)].add(val)
                

        return True