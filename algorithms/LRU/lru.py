class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None


class LRUCache:
    def __init__(self, limit):
        self.limit = limit
        self.hash = {}
        self.head = None
        self.end = None

    def get(self, key):
        node = self.hash.get(key)
        if node is None:
            return None
        self.refresh_node(node)
        return node.value

    def put(self, key, value):
        node = self.hash.get(key)
        if node is None:
            if len(self.hash) >= self.limit:
                self.remove(self.head.key)
            node = Node(key, value)
            self.add_node(node)
            self.hash[key] = node
        else:
            node.value = value
            self.refresh_node(node)

    def remove(self, key):
        node = self.hash.get(key)
        self.remove_node(node)
        self.hash.pop(key)

    def refresh_node(self, node):
        if node is self.end:
            return
        self.remove_node(node)
        self.add_node(node)

    def remove_node(self, node):
        if node is self.head and node is self.end:
            self.head = None
            self.end = None
        elif node is self.end:
            self.end = self.end.pre
            self.end.next = None
        elif node is self.head:
            self.head = self.head.next
            self.head.pre = None
        else:
            node.pre.next = node.next
            node.next.pre = node.pre
        return node.key

    def add_node(self, node):
        if self.end is not None:
            self.end.next = node
            node.pre = self.end
            node.next = None
        self.end = node
        if self.head is None:
            self.head = node


if __name__ == '__main__':
    lru_cache = LRUCache(5)
    lru_cache.put('001', 'user 01')
    lru_cache.put('002', 'user 02')
    lru_cache.put('003', 'user 03')
    lru_cache.put('004', 'user 04')
    lru_cache.put('005', 'user 05')
    print(lru_cache.get('002'))
    lru_cache.put('004', 'update 004')
    lru_cache.put('006', 'user 06')
    print(lru_cache.get('001'))
    print(lru_cache.get('006'))
