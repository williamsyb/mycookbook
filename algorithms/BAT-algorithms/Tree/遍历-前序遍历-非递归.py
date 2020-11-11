class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def pre_order_traversal(root):  # 前序
    result = []
    stack = []
    stack.append(root)
    while len(stack) != 0:
        node = stack.pop()
        if node is None:
            continue
        result.append(node.val)
        stack.append(node.right)
        stack.append(node.left)
    return result


if __name__ == '__main__':
    from tree import construct_tree

    tree = construct_tree()
    print(pre_order_traversal(tree))
