"""

问题定义
有如下 8 x 8 格子，机器人需要从开始位置走到结束位置,每次只能朝右或朝下走，粉色格子为障碍物，机器人不能穿过，
问机器人从开始位置走到结束位置最多共有多少种走法?
"""
from pprint import pprint
mat = [
    [0] * 8,
    [0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0] * 8
]


class Node:
    __slots__ = 'x', 'y'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def right_node(self):
        return Node(self.x + 1, self.y)

    def down_node(self):
        return Node(self.x, self.y + 1)

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def can_visit(self):
        if self.x > len(mat[0]) - 1 or self.y > len(mat) - 1 or mat[self.y][self.x] == 1:
            return False
        else:
            return True

    def __repr__(self):
        return f'{(self.x, self.y)}'


def solution():
    """深度优先搜索"""
    stack = [Node(0, 0)]
    destination = Node(len(mat) - 1, len(mat[0]) - 1)
    count = 0
    res = []
    route = []
    while len(stack) > 0:
        cur_node = stack.pop()
        route.append(cur_node)
        if destination == cur_node:
            res.append(route[:])
            route = []
            count += 1
        right_node = cur_node.right_node()
        down_node = cur_node.down_node()
        if right_node.can_visit():
            stack.append(right_node)

        if down_node.can_visit():
            stack.append(down_node)
    pprint(res)
    return f"共{count}种走法"


if __name__ == '__main__':
    pprint(solution())
