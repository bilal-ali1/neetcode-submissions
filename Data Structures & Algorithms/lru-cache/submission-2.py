class Node:
    def __init__(self, key: int, val: int):
        self.next = None
        self.prev = None
        self.key  = key
        self.val = val

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        # Right = most recent, left is least recnet
        self.right = Node(0, 0)
        self.left = Node(0, 0)
        self.right.next = self.left
        self.left.prev = self.right
        self.cache = {} # Maping key to nodes
    

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
    
    # insert at right
    def insert(self, node):
        nxt = self.right.next
        nxt.prev = node
        node.next = nxt
        self.right.next = node
        node.prev = self.right
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            toRemove = self.left.prev
            del self.cache[toRemove.key]
            self.remove(toRemove)
            

