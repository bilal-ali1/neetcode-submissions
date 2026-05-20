class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev, self.nxt = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.leastUsed = Node(0, 0)
        self.mostUsed = Node(0, 0)

        self.leastUsed.nxt, self.mostUsed.prev = self.mostUsed, self.leastUsed
    
    def insert(self, node):
        prev = self.mostUsed.prev
        prev.nxt = node
        node.prev = prev
        node.nxt = self.mostUsed
        self.mostUsed.prev = node

    def remove(self, node):
        prev = node.prev
        nxt = node.nxt
        prev.nxt = nxt
        nxt.prev = prev



    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val
        
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            del self.cache[self.leastUsed.nxt.key]
            self.remove(self.leastUsed.nxt)
