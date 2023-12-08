import heapq, sys
from collections import defaultdict

input_num = sys.stdin.readline
INF = float('inf')


def dijkstra(graph, first):
    distances[first] = 0
    queue = []
    heapq.heappush(queue, (distances[first], first))

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]: continue

        for node, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[node]:
                distances[node] = distance
                heapq.heappush(queue, (distance, node))


v, e = map(int, input_num().split())
adj_list = {i: [] for i in range(1, v + 1)}
start = int(input_num())
distances = {i: INF for i in range(1, v + 1)}

for _ in range(e):
    u, v, w = map(int, input_num().split())
    adj_list[u].append((v, w))

dijkstra(adj_list, start)
for i in range(1, v + 1):
    print("INF" if distances[i] == INF else distances[i])