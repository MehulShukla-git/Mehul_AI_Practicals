from collections import deque
import heapq

# Graph with weights
g = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2)],
    'C': [('G', 3)],
    'D': [('G', 1)],
    'G': []
}

# Heuristic values
h = {
    'A': 4,
    'B': 2,
    'C': 2,
    'D': 1,
    'G': 0
}

# A* Algorithm
def astar(start, goal):
    pq = [(0, start, 0, [start])]

    while pq:
        f, node, cost, path = heapq.heappop(pq)

        if node == goal:
            return path, cost

        for nb, w in g[node]:
            heapq.heappush(
                pq,
                (cost + w + h[nb], nb, cost + w, path + [nb])
            )

# BFS Algorithm
def bfs(start, goal):
    q = deque([(start, [start])])

    while q:
        node, path = q.popleft()

        if node == goal:
            return path

        for nb, w in g[node]:
            q.append((nb, path + [nb]))

# Run algorithms
p1, c = astar('A', 'G')
p2 = bfs('A', 'G')

print("A*:", *p1, "Cost:", c)
print("BFS:", *p2)
