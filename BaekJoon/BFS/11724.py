import sys
from collections import deque

input = sys.stdin.readline

N, M = list(map(int, input().split()))

adj = [[] for _ in range(N)]  # 인접 리스트

# 양방향 간선 정보 입력
for _ in range(M):
    u, v = list(map(int, input().split()))  # M줄의 양 끝점 U, V
    adj[u - 1].append(v - 1)
    adj[v - 1].append(u - 1)

visit = [False] * N
cnt = 0  # 연결 요소의 개수

# 각 노드에 대해 BFS 시작
for i in range(N):
    if visit[i]:
        continue

    # 새로운 연결 요소 발견 시 카운트 증가
    cnt += 1

    # BFS를 위한 큐 초기화
    queue = deque([i])
    visit[i] = True

    while queue:
        u = queue.popleft()

        for v in adj[u]:
            if not visit[v]:
                queue.append(v)
                visit[v] = True

print(cnt)
