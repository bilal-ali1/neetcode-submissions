class ListNode:
    def __init__(self, key, val, next):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:
    def __init__(self):
        self.HashMap = [ListNode(-1, -1, None) for i in range(10**4)]

    def put(self, key: int, value: int) -> None:
        curr = self.HashMap[key % (10**4)]
        while curr:
            if curr.key == key:
                curr.val = value
                break
            if not curr.next:
                curr.next = ListNode(key, value, None)
                break
            curr = curr.next

    def get(self, key: int) -> int:
        curr = self.HashMap[key % (10**4)]
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        curr = self.HashMap[key % (10**4)]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                break
            curr = curr.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)