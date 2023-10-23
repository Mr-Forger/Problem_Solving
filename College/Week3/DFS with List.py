graph = [[2, 1], [3, 0], [3, 0], [9, 8, 2, 1], [5], [7, 6, 4], [7, 5], [6, 5], [3], [3]]
n = len(graph)
visited = [False for i in range(n)]

def dfs(v):
    visited[v] = True
    print(v, '', end='')
    for w in graph[v]:
        if not visited[w]:
            dfs(w)

print("dfs 순서")

for j in range(n):
    if not visited[j]:
        dfs(j)