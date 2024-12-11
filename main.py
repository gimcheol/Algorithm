import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

adj = [[] for _ in range(N)]

for _ in range(M):
    a, b = list(map(int, input().split())) # 연결 요소 개수
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)

visit = [False] * N
cnt = 0 # 연결 요소의 개수

# BFS
for i in range(N):
    if visit[i]:
        continue

    # 새로운 연결 요소 발견시 개수 증가
    cnt +=1

    queue = deque([i])
    visit[i] = True

    while queue:
        a = queue.popleft()

        for v in adj[a]:
            if not visit[v]:
                queue.append(v)
                visit[v] = True

print(cnt)