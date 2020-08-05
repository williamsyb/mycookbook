# -*- coding UTF-8 -*-
# @project : python03
# @Time    : 2020/6/22 13:49
# @Author  : Yibin Sun
# @Email   : sunyibin@orientsec.com.cn
# @File    : lru_cache.py
# @Software: PyCharm


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
        if node is not None:
            self.refresh_node(node)
            return node.value
        else:
            return None

    def put(self, key, value):
        node = self.hash.get(key)
        if node is not None:
            node.value = value
            self.refresh_node(node)
        else:
            if len(self.hash) >= self.limit:
                self.remove(self.head.key)
            n_node = Node(key, value)
            self.add_node(n_node)
            self.hash[key] = n_node

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
            self.head.next.pre = None
            self.head = self.head.next
        elif self.end is node:
            self.end.pre.next = None
            self.end = self.end.pre
        else:
            node.pre.next = node.next
            node.next.pre = node.pre
        return node.key

    def add_node(self, node):
        if self.end is None:
            pass
        self.end.next = node
        node.pre = self.end
        self.end = node
        if self.head is None:
            self.head = node


if __name__ == '__main__':
    lru_cache = LRUCache(5)
    lru_cache.put('001', 'user 001')
    lru_cache.put('002', 'user 002')
    lru_cache.put('003', 'user 003')
    lru_cache.put('004', 'user 004')
    lru_cache.put('005', 'user 005')
    print(lru_cache.get('003'))
    lru_cache.put('004', 'user 004 update')
    lru_cache.put('005', 'user 005')
