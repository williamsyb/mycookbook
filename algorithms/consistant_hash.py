# -*- coding: utf-8 -*-
# 一致性哈希(hash)
# https://www.bilibili.com/video/av48709993?t=3054
# https://reishin.me/python-consistent-hash/

import hashlib

content = """In computer science, consistent hashing is a special kind of 
hashing such that when a hash table is resized, only K/n keys need to be 
remapped on average, where K is the number of keys, and n is the number of 
slots. In contrast, in most traditional hash tables, a change in the number 
of array slots causes nearly all keys to be remapped because the mapping 
between the keys and the slots is defined by a modular operation."""

servers = [
    "10.10.1.1",
    "10.10.2.2",
    "10.10.3.3",
    "10.10.4.4",
]


class HashRing:
    def __init__(self, nodes=None, replicas=3):
        self.replicas = replicas
        self.ring = dict()
        self._sorted_keys = []

        if nodes:
            for node in nodes:
                self.add_node(node)

    def add_node(self, node):
        """
        Adds a `node` to the hash ring (including a number of replicas)
        """
        for i in range(self.replicas):
            virtual_node = f"{node}#{i}"
            key = self.gen_key(virtual_node)
            self.ring[key] = node
            self._sorted_keys.append(key)
            # print(f"{virtual_node} --> {key} --> {node}")

        self._sorted_keys.sort()
        # print([self.ring[key] for key in self._sorted_keys])

    def remove_node(self, node):
        """
        Removes `node` from the hash ring and its replicas
        """
        for i in range(self.replicas):
            key = self.gen_key(f"{node}#{i}")
            del self.ring[key]
            self._sorted_keys.remove(key)

    def get_node(self, string_key):
        """
        Given a string key a corresponding node in the hash ring is returned.

        If the hash ring is empty, `None` is returned.
        """
        return self.get_node_pos(string_key)[0]

    def get_node_pos(self, string_key):
        """
        Given a string key a corresponding node in the hash ring is returned
        along with it's position in the ring.

        If the hash ring is empty, (`None`, `None`) is returned.
        """
        if not self.ring:
            return None, None

        key = self.gen_key(string_key)
        nodes = self._sorted_keys
        for i in range(len(nodes)):
            node = nodes[i]
            if key < node:
                return self.ring[node], i

        # 如果key > node，那么让这些key落在第一个node上就形成了闭环
        return self.ring[nodes[0]], 0

    def gen_key(self, string_key):
        """
        Given a string key it returns a long value, this long value represents
        a place on the hash ring
        """
        m = hashlib.md5()
        m.update(string_key.encode('utf-8'))
        res = m.hexdigest()
        print(f'string_key:{string_key}, res:{res}')
        return res


def consistent_hash(replicas):
    hr = HashRing(servers, replicas)
    words = content.split()

    database = {s: [] for s in servers}

    for w in words:
        database[hr.get_node(w)].append(w)

    # print(f"words={len(words)}\n")

    for node, result in database.items():
        print(f"{node}={len(result)}\nresult={result}")


if __name__ == '__main__':
    consistent_hash(3)
