class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = {}
        self.isEnd = False

class PrefixTree:
    def __init__(self):
        self.root = Node()
        
    def insert(self, word: str) -> None:
        lastIdx = len(word) - 1
        ctr = 0
        currNode = self.root
        if word:
            while ctr <= lastIdx:
                if (not currNode.children) or not (word[ctr] in currNode.children):
                    newNode = Node(word[ctr])
                    if ctr == lastIdx:
                        newNode.isEnd = True
                    currNode.children[word[ctr]] = newNode
                    currNode = newNode
                    ctr += 1
                else: 
                    newNode = currNode.children[word[ctr]]
                    currNode = newNode
                    ctr += 1
        currNode.isEnd = True

    def search(self, word: str) -> bool:
        currNode = self.root
        for char in word:
            if not (char in currNode.children):
                return False
            currNode = currNode.children[char]
        if currNode.isEnd:
            return True    
        return False            

    def startsWith(self, prefix: str) -> bool:
        currNode = self.root
        for char in prefix:
            if not (char in currNode.children):
                return False
            currNode = currNode.children[char]
        return True
        