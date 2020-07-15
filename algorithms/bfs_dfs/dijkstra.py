import heapq

import math

graph_g = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
    'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
    'E': {'C': 8, 'D': 3},
    'F': {'D': 6}
}


def dijkstra(graph, s):
    pqueue = []
    heapq.heappush(pqueue, (0, s))
    seen = set()
    parent = {s: None}
    distance = {s: 0}
    print(pqueue)
    while len(pqueue) > 0:
        print(pqueue)
        dist, vertex = heapq.heappop(pqueue)
        seen.add(vertex)
        nodes = graph_g[vertex].keys()

        for w in nodes:
            if w not in seen:
                if dist + graph[vertex][w] < distance.get(w, math.inf):
                    # print(f'push {w}')
                    heapq.heappush(pqueue, (dist + graph[vertex][w], w))
                    parent[w] = vertex
                    distance[w] = dist + graph[vertex][w]

    return parent, distance


def test(graph, s):
    pqueue = []
    heapq.heappush(pqueue, (0, s))
    seen = set()
    parent = {s: None}
    distance = {}
    while len(pqueue) > 0:
        dist, vertex = heapq.heappop(pqueue)
        nodes = graph[vertex].keys()
        for w in nodes:
            if w not in seen:
                if dist + graph[vertex][w] < distance.get(w, math.inf):
                    heapq.heappush(pqueue, (dist + graph[vertex][w], w))
                    parent[w] = vertex
                    distance[w] = dist + graph[vertex][w]
    return parent, distance


def test2(graph, s):
    pqueue = []
    heapq.heappush(pqueue, (0, s))
    seen = set()
    distance = {s: 0}
    parent = {s: None}
    while len(pqueue) > 0:
        dist, vertex = heapq.heappop(pqueue)
        nodes = graph[vertex].keys()
        for w in nodes:
            if w not in seen and dist + graph[vertex][w] < distance.get(w, math.inf):
                heapq.heappush(pqueue, (dist + graph[vertex][w], w))
                distance[w] = dist + graph[vertex][w]
                parent[w] = vertex
    return parent, distance


if __name__ == '__main__':
    parents, distances = test2(graph_g, 'A')
    print(parents)
    print(distances)
