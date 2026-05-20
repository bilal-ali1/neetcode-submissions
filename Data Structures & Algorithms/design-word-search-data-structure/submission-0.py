class Node:
        def __init__(self):
            self.children = {}
            self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = Node()
        
        

    def addWord(self, word: str) -> None:
        currNode = self.root
        for i in range(len(word)):
            if word[i] in currNode.children:
                currNode = currNode.children[word[i]]
            else:
                newNode = Node()
                currNode.children[word[i]] = newNode
                currNode = newNode
        currNode.isEnd = True
            

    def search(self, word: str) -> bool:
        def dfs(j, node):
            currNode = node
            for i in range(j, len(word)):
                if word[i] in currNode.children:
                    currNode = currNode.children[word[i]]
                elif word[i] == '.':
                    for child in currNode.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    return False
            return currNode.isEnd
        return dfs(0, self.root)
        
