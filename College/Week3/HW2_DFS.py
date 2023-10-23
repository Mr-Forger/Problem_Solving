adj_list = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 4],
    3: [1, 4],
    4: [2, 3]
}

n = len(adj_list)
visited = [False for i in range(n)]

def dfs(v):
    visited[v] = True
    print(f"{v}", end=' ')
    for w in adj_list[v]:
        if not visited[w]:
            dfs(w)

print("dfs 순서")
for j in range(n):
    if not visited[j]:
        dfs(j)

