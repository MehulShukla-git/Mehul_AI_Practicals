graph = {
    'A': {'B': 2, 'C': 4},   
    'B': {'D': 3, 'E': 5},   
    'C': {'F': 6},           
    'D': {},
    'E': {'F': 4},           
    'F': {}
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 3,
    'E': 2,
    'F': 0
}

start = 'A'
goal = 'F'

open_list = [start]
closed_list = []

g = {start: 0}
parent = {start: None}

while open_list:
    current = open_list[0]
    for node in open_list:
        if g[node] + heuristic[node] < g[current] + heuristic[current]:
            current = node

    if current == goal:
        break

    open_list.remove(current)
    closed_list.append(current)

    for neighbor in graph[current]:
        cost = g[current] + graph[current][neighbor]

        if neighbor in closed_list:
            continue

        if neighbor not in open_list or cost < g.get(neighbor, 999):
            g[neighbor] = cost
            parent[neighbor] = current
            if neighbor not in open_list:
                open_list.append(neighbor)

path = []
node = goal
while node is not None:
    path.append(node)
    node = parent[node]

path.reverse()

print("Path found:", path)
print("Total cost:", g[goal])