from collections import deque

N = int(input()) # 컴퓨터 수
M = int(input()) # 연결되어 있는 컴퓨터 쌍 수

adj = [[] for _ in range(N)]

for _ in range(M):
    a, b = list(map(int, input().split())) # 연결된 컴퓨터 쌍
    adj[a - 1].append(b - 1) # a와 연결된 노드 b 추가
    adj[b - 1].append(a - 1) # b와 연결된 노드 a 추가

# BFS 시작
visit = [False] * N # 방문 여부 기록
cnt = 0 # 감염된 컴퓨터 수
queue = deque([0]) # 1번 컴퓨터(인덱스 0)부터 탐색 시작
visit[0] = True # 방문 처리

while queue:
    u = queue.popleft()

    for j in adj[u]: # 연결된 노드 순회
        if not visit[j]:
            visit[j] = True
            queue.append(j) # 큐에 추가
            cnt += 1 # 감염된 컴퓨터 수 증가

print(cnt)


