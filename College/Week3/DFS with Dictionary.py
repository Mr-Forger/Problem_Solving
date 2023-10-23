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

def dfs(v):
    visited[v] = True
    print(f"{v}", end=' ')
    for w in graph[v]:
        if not visited[w]:
            dfs(w)

print("dfs 순서")
for j in range(n):
    if not visited[j]:
        dfs(j)
