# 广度优先搜索
from pprint import pprint

graph_g = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E', 'F'],
    'E': ['C', 'D'],
    'F': ['D']
}


def bfs(graph, s):
    # bfs广度优先需要使用队列
    queue = list()
    queue.append(s)
    seen = set()
    seen.add(s)
    parent = {s: None}
    while len(queue) > 0:
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
                parent[w] = vertex
        print(vertex)
    return parent


def print_line():
    print('-' * 30)


if __name__ == '__main__':
    parent = bfs(graph_g, 'A')
    print_line()
    for key in parent:
        print(f'{key}:', parent[key])
    # pprint(parent)
    print_line()
    # 通过parent就可以求出两点之间最短的路径
    # 因为上面定义了图的头结点是 'A'，则'A'到'D'的路径通过以下方式得到 ->  A B D
    node = 'D'
    while node:
        print(node)
        node = parent[node]
