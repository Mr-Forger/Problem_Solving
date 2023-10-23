graph = {
    0: [2, 1],
    1: [3, 0],
    2: [3, 0],
    3: [9, 8, 2, 1],
    4: [5],
    5: [7, 6, 4],
    6: [7, 5],
    7: [6, 5],
    8: [3],
    9: [3]
}

n = len(graph)
visited = [False for i in range(n)]

def bfs(v):
    queue = []
    visited[v] = True
    queue.append(v)
    while len(queue) != 0:
        u = queue.pop(0)
        print(f"{u}", end=' ')
        for w in graph[u]:
            if not visited[w]:
                visited[w] = True
                queue.append(w)

print("BFS\n")
for i in range(n):
    if not visited[i]:
        bfs(i)