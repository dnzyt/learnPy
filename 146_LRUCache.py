class Node(object):
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value

class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.d = dict()
        

    def get(self, key):
        if key in self.d:
            node = self.d[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = self.head.next
            self.head.next.prev = node
            self.head.next = node
            node.prev = self.head
            return node.value
        else:
            return -1


    def put(self, key, value):
        if key in self.d:
            self.d[key].value = value
            self.get(key)
            return
        if self.count == self.capacity:
            self.d[key] = self.tail.prev
            k = self.tail.prev.key
            self.get(k)
            self.head.next.key = key
            self.head.next.value = value
            del self.d[k]
        else:
            self.count += 1
            node = Node(key, value)
            self.d[key] = node
            self.head.next.prev = node
            node.next = self.head.next
            self.head.next = node
            node.prev = self.head



