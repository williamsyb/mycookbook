class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# # 非递归
def in_order_traversal(root):  # 中序
    res = []
    stack = []
    if root is None:
        return res
    cur = root
    while len(stack) != 0 or cur is not None:
        while cur is not None:
            stack.append(cur)
            cur = cur.left
        node = stack.pop()
        res.append(node.val)
        cur = node.right
    return res


# 非递归
def in_order_traversal2(root):  # 中序
    res = []
    stack = []
    if root is None:
        return res
    cur = root
    while len(stack) != 0 or cur is not None:
        # 1.先将左分支都存入stack
        while cur is not None:
            stack.append(cur)
            cur = cur.left
        # 2.将左分支拿出一个存入result
        node = stack.pop()
        res.append(node.val)
        # 3.每次存入后都查一下是否有右分支，
        # 有的话设置cur指针，在下一轮循环中再次试图将其所有左分支存入stack
        if node.right:
            cur = node.right
    return res


# 递归
def in_order(root, res=[]):
    if root is None:
        return root

    in_order(root.left)
    res.append(root.val)
    in_order(root.right)
    return res


def make_tree():
    """
              1
                \
                 2
                /
              3
    """
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    return root


if __name__ == '__main__':
    from tree import construct_tree

    tree = construct_tree()
    # tree = make_tree()
    # print(in_order(tree))
    print(in_order_traversal2(tree))
