adj_list = {
    0: [1, 2, 3],
    1: [0, 3],
    2: [0, 3],
    3: [0, 1, 2]
}

n = len(adj_list)
visited = [False for i in range(n)]

def bfs(v):
    queue = []
    visited[v] = True
    queue.append(v)
    while len(queue) != 0:
        u = queue.pop(0)
        print(f"{u}", end=' ')
        for w in adj_list[u]:
            if not visited[w]:
                visited[w] = True
                queue.append(w)

print("BFS 순서\n")
for i in range(n):
    if not visited[i]:
        bfs(i)