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
            return
        self.refresh_node(node)
        return node.value

    def put(self, key, value):
        node = self.hash.get(key)
        if node is None:
            if len(self.hash) >= self.limit:
                self.remove(self.head.key)

            new_node = Node(key, value)
            self.add_node(new_node)
            self.hash[key] = new_node
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
        if self.head is node and self.end is node:
            self.head = None
            self.end = None
        elif self.head is node:
            self.head = self.head.next
            self.head.pre = None
        elif self.end is node:
            self.end = self.end.pre
            self.end.next = None
        else:
            node.pre.next = node.next
            node.next.pre = node.pre
        # return node.key

    def add_node(self, node):
        if self.end is not None:
            self.end.next = node
            node.pre = self.end
            node.next = None
        self.end = node
        if self.head is None:
            self.head = node


if __name__ == '__main__':
    cache = LRUCache(5)
    cache.put('01', 'user 01')
    cache.put('02', 'user 02')
    cache.put('03', 'user 03')
    cache.put('04', 'user 04')
    cache.put('05', 'user 05')
    print(cache.get('02'))
    print(cache.get('03'))
    cache.put('06', 'user 06')
    cache.put('04', 'new user 04')
    print(cache.get('04'))
    print(cache.get('01'))
