class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False
    
    def addWord(self, word):
        curr = self
        for i in range(len(word)):
            if word[i] in curr.children:
                curr = curr.children[word[i]]
            else:
                curr.children[word[i]] = Node()
                curr = curr.children[word[i]]
        curr.isEnd = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS = len(board)
        COLS = len(board[0])
        res = set()
        visit = set()

        root = Node()
        for word in words:
            root.addWord(word)

        def dfs(row, col, currNode, word):
            if (row >= ROWS or col >= COLS or row < 0 or col < 0 or board[row][col] not in currNode.children or (row, col) in visit):
                return
            
            visit.add((row, col))
            currNode = currNode.children[board[row][col]]
            word = word + board[row][col]
            
            if currNode.isEnd:
                 res.add(word)
                
            dfs(row + 1, col, currNode, word)
            dfs(row - 1, col, currNode, word)
            dfs(row, col + 1, currNode, word)
            dfs(row, col - 1, currNode, word)
            
            visit.remove((row, col))


        for row in range(ROWS):
            for col in range(COLS):
                dfs(row, col, root, "")
        return list(res)
                
                    