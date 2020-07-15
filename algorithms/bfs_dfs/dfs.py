graph_g = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E', 'F'],
    'E': ['C', 'D'],
    'F': ['D']
}


def dfs(graph, s):
    stack = list()
    stack.append(s)
    seen = set()
    seen.add(s)
    while len(stack) > 0:
        vertex = stack.pop()
        nodes = graph[vertex]
        for node in nodes:
            if node not in seen:
                stack.append(node)
                seen.add(node)
        print(vertex)


if __name__ == '__main__':
    dfs(graph_g, 'A')
