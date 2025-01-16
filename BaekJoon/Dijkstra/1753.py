# 방향그래프가 주어진 시작점에서 다른 모든 정점으로의
# 최단 경로를 구하는 프로그램을 작성하시오. 단, 모든 간선의 가중치는 10이하 자연수

import sys
from queue import PriorityQueue

input = sys.stdin.readline

# 정점 개수 : V, 간선 개수 : E
V, E = list(map(int, input().split()))
K = int(input()) - 1 # 시작 정점, 인접리스트에 맞추기위해 -1

adj = [[] for _ in range(V)]

for _ in range(E):
    u, v, w = list(map(int, input().split())) # u, v : 정점 , w : 거리
    adj[u - 1].append((v - 1, w))

# 다익스트라
dist = [1e9] * V    # 최단거리 배열 (큰수로 초기화)
pq = PriorityQueue()

dist[K] = 0
pq.put((0, K)) # 최단거리와 노드의 정점번호를 넣어줌

while pq.qsize() != 0:
    d, u = pq.get()

    if d != dist[u]:
        continue

    for v, w in adj[u]:
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            pq.put((dist[v], v))

for i in range(V):
    if dist[i] == 1e9:
        print("INF")
    else:
        print(dist[i])
