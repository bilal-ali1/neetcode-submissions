class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        squares = {}
        for row in range(len(board)):
            rows[row] = set()
            for col in range(len(board[0])):
                if not col in cols:
                    cols[col] = set()
                if not (row, col) in squares:
                    squares[(row, col)] = set()
                if not board[row][col] == ".":
                    if board[row][col] in rows[row]:
                        return False
                    if board[row][col] in cols[col]:
                        return False
                    if board[row][col] in squares[(row // 3, col // 3)]:
                        return False
                    rows[row].add(board[row][col])
                    cols[col].add(board[row][col])
                    squares[(row // 3, col // 3)].add(board[row][col])
        return True

         

