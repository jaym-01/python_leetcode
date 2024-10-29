# uses a doubly linked list to store the order of keys in the LRU queue
# enables constant time for changing order of elements in the queue
# uses a dictionary to store key value pairs
# enables constant access time to a value

class LLNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.store = {}
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        val = -1
        if key in self.store:
            val = self.store[key][0]
            if self.head.val == key:
                return val
            if self.tail.val == key and self.head.val != key:
                self.tail = self.tail.prev
                self.tail.next = None
            node = self.store[key][1]

            if node.prev: node.prev.next = node.next
            if node.next: node.next.prev = node.prev
            node.next = self.head
            self.head.prev = node
            self.head = node
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.store[key] = (value, self.store[key][1])

            if self.head.val == key:
                return

            if self.tail.val == key:
                self.tail = self.tail.prev
                self.tail.next = None
            node = self.store[key][1]

            if node.prev: node.prev.next = node.next
            if node.next: node.next.prev = node.prev
            node.next = self.head
            self.head.prev = node
            self.head = node

            return

        node = LLNode(key)
        if len(self.store) < self.size:
            if not self.head and not self.tail:
                self.head = node
                self.tail = node
            else:
                node.next = self.head
                self.head.prev = node
                self.head = node
        else:
            rm = self.tail.val
            if self.tail.val == self.head.val:
                self.tail = node
                self.head = node
            else:
                self.tail = self.tail.prev
                self.tail.next = None

                node.next = self.head
                self.head.prev = node
                self.head = node
            del self.store[rm]

        self.store[key] = (value, node)
