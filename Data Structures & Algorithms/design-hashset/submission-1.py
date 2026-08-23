class ListNode:
    def __init__(self, key, next):
        self.key = key
        self.next = next

class MyHashSet:
    def __init__(self):
        self.Hashset = [ListNode(-1, None) for i in range(10**4)]

    def add(self, key: int) -> None:
        if not self.contains(key):
            curr = self.Hashset[key % (10**4)]
            while curr.next:
                curr = curr.next
            curr.next = ListNode(key, None)


    def remove(self, key: int) -> None:
        if self.contains(key):
            curr = self.Hashset[key % (10**4)]
            while curr.next:
                if curr.next.key == key:
                    curr.next = curr.next.next
                    break
                curr = curr.next


    def contains(self, key: int) -> bool:
        curr = self.Hashset[key % (10**4)]
        while curr:
            if curr.key == key:
                return True
            curr = curr.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)