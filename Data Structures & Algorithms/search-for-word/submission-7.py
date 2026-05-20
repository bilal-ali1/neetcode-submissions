class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def searchWord(row, col, i, visited):
            if (row < 0 or col < 0 or row >= rows or col >= cols or 
                    board[row][col] != word[i] or (row, col) in visited):
                return False
            if board[row][col] == word[i] and i == len(word) - 1:
                return True
            
            visited.add((row, col))

            found = (searchWord(row + 1, col, i + 1, visited) or searchWord(row - 1, col, i + 1, visited) or 
                searchWord(row, col + 1, i + 1, visited) or searchWord(row, col - 1, i + 1, visited))
            
            visited.remove((row, col))
            return found
            


        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    if searchWord(row, col, 0, set()):
                        return True
        return False
            
        