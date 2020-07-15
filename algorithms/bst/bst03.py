class Node:
    def __init__(self, data):
        self.data = data
        self.lc = None
        self.rc = None


class BST:
    def __init__(self, node_list):
        self.root = Node(node_list[0])
        for data in node_list[1:]:
            self.insert(data)

    def search(self, node, parent, data):
        if node is None:
            return False, node, parent
        if node.data == data:
            return True, node, parent
        if data > node.data:
            return self.search(node.rc, node, data)
        else:
            return self.search(node.lc, node, data)

    def insert(self, data):
        flag, n, p = self.search(self.root, self.root, data)
        if not flag:
            new_node = Node(data)
            if data > p.data:
                p.rc = new_node
            else:
                p.lc = new_node

    def delete(self, data):
        flag, n, p = self.search(self.root, self.root, data)
        if not flag:
            print('未找到', data)
        else:
            if n.lc is None:
                if n == p.lc:
                    p.lc = n.rc
                else:
                    p.rc = n.rc
            elif n.rc is None:
                if n == p.rc:
                    p.rc = n.lc
                else:
                    p.lc = n.lc
                del n
            else:
                pre = n.rc
                if pre.lc is None:
                    n.data = pre.data
                    n.rc = pre.rc
                    del pre
                else:
                    next = pre.lc
                    while next.lc:
                        pre = next
                        next = next.lc
                    n.data = next.data
                    pre.lc = next.rc
                    del next

    def inOrderTraverse(self, node):
        if node:
            self.inOrderTraverse(node.lc)
            print(node.data)
            self.inOrderTraverse(node.rc)

    def preOrderTraverse(self, node):
        if node:
            print(node.data)
            self.preOrderTraverse(node.lc)
            self.preOrderTraverse(node.rc)

    def postOrderTraverse(self, node):
        if node:
            self.postOrderTraverse(node.lc)
            self.postOrderTraverse(node.rc)
            print(node.data)


if __name__ == '__main__':
    a = [49, 38, 65, 97, 60, 76, 13, 27, 5, 1]
    bst = BST(a)
    bst.inOrderTraverse(bst.root)
    print('-' * 30)
    bst.delete(49)
    bst.inOrderTraverse(bst.root)
