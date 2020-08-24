class Array(object):

    def __init__(self, size=32, init=None):
        self._size = size
        self._items = [init] * self._size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return self._size

    def clear(self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value

    def __contains__(self, item):
        return item in self._items

    def __iter__(self):
        for item in self._items:
            yield item


class Slot(object):
    """定义一个 hash 表 数组的槽
    注意，一个槽有三种状态，看你能否想明白
    1.从未使用 HashMap.UNUSED。此槽没有被使用和冲突过，查找时只要找到 UNUSED 就不用再继续探查了
    2.使用过但是 remove 了，此时是 HashMap.EMPTY，该探查点后边的元素扔可能是有key
    3.槽正在使用 Slot 节点
    """

    def __init__(self, key, value):
        self.key, self.value = key, value


class HashTable(object):
    # 表示从未被使用过
    UNUSED = None
    # 使用过，但是被删除了
    EMPTY = Slot(None, None)

    def __init__(self):
        self._table = Array(8, init=HashTable.UNUSED)
        self.length = 0

    # 负载因子
    @property
    def _load_factor(self):
        return self.length / float(len(self._table))

    def __len__(self):
        return self.length

    # 哈希函数 用内置的哈希哈数进行哈希一下，然后对数组长度取模
    def _hash(self, key):
        return abs(hash(key)) % len(self._table)

    def _find_key(self, key):
        # 得到第一个值的位置
        index = self._hash(key)
        _len = len(self._table)
        # 当这个槽是使用过的，才接着往下找；如果是未使用过的，这个key肯定不存在
        while self._table[index] is not HashTable.UNUSED:
            # 槽使用过，但是被删除了
            if self._table[index] is HashTable.EMPTY:
                # cpython解决哈希冲突的一种方式
                index = (index * 5 + 1) % _len
                continue
            elif self._table[index].key == key:
                return index
            else:
                index = (index * 5 + 1) % _len
        return None

    # 检测槽是否能被插入
    def _slot_can_insert(self, index):
        return (self._table[index] is HashTable.EMPTY or self._table[index] is HashTable.UNUSED)

    # 找到能被插入的槽的index
    def _find_slot_insert(self, key):
        # 得到第一个值的位置
        index = self._hash(key)
        _len = len(self._table)
        while not self._slot_can_insert(index):
            index = (index * 5 + 1) % _len
        return index

    # in 操作符
    def __contains__(self, key):
        index = self._find_key(key)
        return index is not None

    def add(self, key, value):
        if key in self:
            index = self._find_key(key)
            # 更新值
            self._table[index].value = value
            return False
        else:
            index = self._find_slot_insert(key)
            self._table[index] = Slot(key, value)
            self.length += 1
            if self._load_factor > 0.8:
                return self._rehash()
            return True

    def _rehash(self):
        oldtable = self._table
        newsize = len(self._table) * 2
        # 新的table
        self._table = Array(newsize, HashTable.UNUSED)
        self.length = 0
        for slot in oldtable:
            if slot is not HashTable.UNUSED and slot is not HashTable.EMPTY:
                index = self._find_slot_insert(slot.key)
                self._table[index] = slot
                self.length += 1

    def get(self, key, default=None):
        index = self._find_key(key)
        if index is None:
            return default
        else:
            return self._table[index].value

    def remove(self, key):
        index = self._find_key(key)
        if index is None:
            raise KeyError
        value = self._table[index].value
        self.length -= 1
        # 把槽设置为空槽
        self._table[index] = HashTable.EMPTY
        return value

    def __iter__(self):
        for slot in self._table:
            if slot not in (HashTable.UNUSED, HashTable.EMPTY):
                yield slot.value


class DictADT(HashTable):
    def __setitem__(self, key, value):
        self.add(key, value)

    def __getitem__(self, key):
        if key not in self:
            raise KeyError()
        else:
            self.get(key)

    def _iter_slot(self):
        for slot in self._table:
            if slot not in (HashTable.UNUSED, HashTable.EMPTY):
                yield slot

    def items(self):
        for slot in self._iter_slot():
            yield (slot.key, slot.value)

    def keys(self):
        for slot in self._iter_slot():
            yield slot.key

    def values(self):
        for slot in self._iter_slot():
            yield slot.value


if __name__ == '__main__':
    my_dict = DictADT()
    my_dict['name'] = 'william'
    my_dict['age'] = 30
    # print(list(my_dict.values()))
    # print(list(my_dict.keys()))
    # print(list(my_dict.items()))
    my_dict.add('sex', 'male')
    print(my_dict.get('sex'))
    print(my_dict['name'])
    print(list(my_dict.values()))
    print(list(my_dict.keys()))
    print(list(my_dict.items()))
    print(list(my_dict.items()))
