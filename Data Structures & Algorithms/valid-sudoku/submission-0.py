class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        visited_rows = {i:set() for i in range(9)}
        visited_cols = {i:set() for i in range(9)}
        rows, cols = len(board), len(board[0])
        for r in range(rows):
            for c in range(cols):
                val = board[r][c]
                if val == ".":
                        continue
                if val in visited_rows[r] or val in visited_cols[c]:
                    return False
                visited_rows[r].add(val)
                visited_cols[c].add(val)

        neighbors = [(0,0),(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]
        for r in range(1, 9, 3):
            for c in range(1, 9, 3):
                visited = set()
                for x,y in neighbors:
                    val = board[r+x][c+y]
                    if val == ".":
                        continue
                    if val in visited:
                        return False
                    visited.add(val)
        return True
