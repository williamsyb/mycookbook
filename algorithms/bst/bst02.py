class Node:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


class BST:
    def __init__(self, array):
        self.root = Node(array[0])
        for data in array[1:]:
            self.insert(data)

    def search(self, node: Node, parent, data):
        if node is None:
            return False, node, parent
        if node.data == data:
            return True, node, parent
        if data > node.data:
            return self.search(node.rchild, node, data)
        else:
            return self.search(node.lchild, node, data)

    def insert(self, data):
        flag, n, p = self.search(self.root, self.root, data)
        if not flag:
            new_node = Node(data)
            if data > p.data:
                p.rchild = new_node
            else:
                p.lchild = new_node

    def delete(self, root, data):
        flag, n, p = self.search(root, root, data)
        if not flag:
            print('未找到，删除失败')
        else:
            if n.lchild is None:
                if n == p.lchild:
                    p.lchild = n.rchild
                else:
                    p.rchild = n.rchild
                del n
            elif n.rchild is None:
                if n == p.lchild:
                    p.lchild = n.lchild
                else:
                    p.rchild = n.lchild
                del n
            else:
                pre = n.rchild
                if pre.lchild is None:
                    n.data = pre.data
                    n.rchild = pre.rchild
                    del pre
                else:
                    next = pre.lchild
                    while next.lchild is not None:
                        pre = next
                        next = next.lchild
                    n.data = next.data
                    pre.lchild = next.rchild
                    del next

    def preOrderTraverse(self, node):
        if node is not None:
            print(node.data)
            self.preOrderTraverse(node.lchild)
            self.preOrderTraverse(node.rchild)

    def inOrderTraverse(self, node):
        if node:
            self.inOrderTraverse(node.lchild)
            print(node.data)
            self.inOrderTraverse(node.rchild)

    def postOrderTraverse(self, node):
        if node:
            self.postOrderTraverse(node.lchild)
            self.postOrderTraverse(node.rchild)
            print(node.data)


if __name__ == '__main__':
    a = [49, 38, 65, 97, 60, 76, 13, 27, 5, 1]
    bst = BST(a)
    bst.inOrderTraverse(bst.root)
    print('-' * 30)
    bst.delete(bst.root, 49)
    bst.inOrderTraverse(bst.root)
