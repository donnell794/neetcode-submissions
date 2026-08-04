class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        if not all([self.check_row(board, row) for row in range(9)]):
            return False

        if not all([self.check_col(board, col) for col in range(9)]):
            return False

        for row in range(1,8,3):
            for col in range(1,8,3):
                if not self.check_box(board, row, col):
                    return False

        return True
        

    def check_row(self, board, r):
        visited = set()
        for y in range(9):
            if board[r][y] == ".": continue
            if board[r][y] in visited:
                return False
            visited.add(board[r][y])
        return True

    def check_col(self, board, c):
        visited = set()
        for x in range(9):
            if board[x][c] == ".": continue
            if board[x][c] in visited:
                return False
            visited.add(board[x][c])

        return True

    def check_box(self, board, r, c):
        visited = set()
        dirs = [
            (0,0),
            (0,1),
            (1,0),
            (1,1),
            (0,-1),
            (-1,0),
            (-1,-1),
            (-1, 1),
            (1,-1),
        ]
        for x,y in dirs:
            if board[r+x][c+y] == ".": continue
            if board[r+x][c+y] in visited:
                return False
            visited.add(board[r+x][c+y])
        return True
        