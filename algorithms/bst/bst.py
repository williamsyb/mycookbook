class Tree:
    def __init__(self, v):
        self.v = v
        self.left: Tree = None
        self.right: Tree = None

    def add(self, v):
        if v > self.v:
            if self.right is None:
                self.right = Tree(v)
            else:
                self.right.add(v)
        else:
            if self.left is None:
                self.left = Tree(v)
            else:
                self.left.add(v)

    def in_order(self, f):
        """
        中序遍历
        :return:
        """
        if self.left:
            self.left.in_order(f)
        f(self.v)
        if self.right:
            self.right.in_order(f)

    def pre_order(self, f):
        """
        先序遍历
        :return:
        """
        f(self.v)
        if self.left:
            self.left.pre_order(f)
        if self.right:
            self.right.pre_order(f)

    def post_order(self, f):
        """
        后序遍历
        :return:
        """
        if self.left:
            self.left.post_order(f)
        if self.right:
            self.right.post_order(f)
        f(self.v)

    def sum(self):
        res = 0

        def get_sum(v):
            nonlocal res
            res += v

        self.in_order(get_sum)
        return res

    def product(self):
        res = 1

        def get_product(v):
            nonlocal res
            res *= v

        self.in_order(get_product)
        return res

    def in_order_g(self):
        if self.left:
            yield from self.left.in_order_g()
        yield self.v
        if self.right:
            yield from self.right.in_order_g()

    def reduce(self, reducer):
        g = self.in_order_g()
        init = next(g)  # 不像之前的sum和product函数需要定义一个初始的res值，这里直接用生成器中的第一个值当init
        for v in g:
            init = reducer(init, v)
        return init

    def map(self, mapper):
        g = self.in_order_g()
        for v in g:
            yield mapper(v)

    def filter(self, f):
        g = self.in_order_g()
        for v in g:
            if f(v):
                yield v

    def __contains__(self, item):
        g = self.in_order_g()
        for v in g:
            if item == v:
                return True
        return False


def get_tree_max_depth(root: Tree):
    if root is None:
        return 0
    return max(get_tree_max_depth(root.left), get_tree_max_depth(root.right))+1


def print_line():
    print('-' * 20)


if __name__ == '__main__':
    # t = Tree(0)
    # t.add(-1)
    # t.add(-2)
    # t.add(1)
    # t.add(2)
    # t.add(-0.5)
    t = Tree(17)
    t.add(7)
    t.add(2)
    t.add(11)
    t.add(9)
    t.add(8)
    t.add(16)
    t.add(35)
    t.add(29)
    t.add(38)

    # t.in_order(print)
    # print('-' * 20)
    # t.pre_order(print)
    # print('-' * 20)
    # t.post_order(print)
    # print_line()
    # print(t.sum())
    # print_line()
    # print(t.product())
    # print_line()
    # print(t.reduce(lambda x, y: x + y))
    # print_line()
    # for ele in t.map(lambda x: x // 4):
    #     print(ele)
    # print_line()
    for ele in t.filter(lambda x: x > 10):
        print(ele)
    print(29+3 in t)
    print(get_tree_max_depth(t))
