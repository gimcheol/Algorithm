import sys
import heapq

input = sys.stdin.readline
INF = float('inf')

# 정점 개수 : V, 간선 개수 : E
V, E = map(int, input().split())
K = int(input()) - 1  # 시작 정점 (1-based → 0-based)

# 그래프 초기화
graph = [[] for _ in range(V)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u - 1].append((v - 1, w))

# 다익스트라 알고리즘
def dijkstra(start):
    dist = [INF] * V
    dist[start] = 0
    pq = [(0, start)]  # (거리, 노드)

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_dist > dist[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return dist

# 최단거리 계산
distances = dijkstra(K)

# 결과 출력
for distance in distances:
    print("INF" if distance == INF else distance)
