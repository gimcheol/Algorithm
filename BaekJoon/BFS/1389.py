import sys
from collections import deque

# 입력을 빠르게 받기 위해 sys.stdin.readline을 사용
input = sys.stdin.readline

# 노드의 수(N)와 간선의 수(M)를 입력받음
N, M = list(map(int, input().split()))

# 각 노드의 인접 리스트 초기화 (N개의 빈 리스트)
adj = [[] for _ in range(N)]

# M개의 간선 정보를 입력받음
for _ in range(M):
    a, b = list(map(int, input().split()))
    adj[a - 1].append(b - 1)  # a와 연결된 노드 b 추가 (0 인덱스로 조정)
    adj[b - 1].append(a - 1)  # b와 연결된 노드 a 추가 (0 인덱스로 조정)

# 초기값 설정: 케빈 베이컨 수의 최소값을 무한대로 설정
min_kevin_bacon = 1e9
# 초기값 설정: 최소 케빈 베이컨 수를 가진 사람 번호를 -1로 설정
min_person = -1

# 모든 노드에 대해 BFS를 수행
for i in range(N):
    visit = [False] * N  # 방문 여부를 체크하기 위한 리스트
    dist = [-1] * N      # 각 노드까지의 거리를 저장하는 리스트

    # BFS에서 사용할 큐 초기화 (현재 노드 i를 큐에 추가)
    queue = deque([i])
    visit[i] = True  # 현재 노드를 방문 처리
    dist[i] = 0      # 현재 노드까지의 거리는 0

    # 큐가 빌 때까지 BFS 수행
    while queue:
        u = queue.popleft()  # 큐에서 노드 u를 꺼냄

        # u와 인접한 모든 노드 v를 탐색
        for v in adj[u]:
            if not visit[v]:  # v가 아직 방문하지 않은 노드일 경우
                queue.append(v)  # 큐에 v 추가
                visit[v] = True   # v를 방문 처리
                dist[v] = dist[u] + 1  # u까지의 거리 + 1로 v까지의 거리 설정

    # 현재 노드 i의 케빈 베이컨 수를 계산 (모든 거리의 합)
    kevin_bacon = sum(dist)

    # 계산된 케빈 베이컨 수가 최소값보다 작으면 갱신
    if min_kevin_bacon > kevin_bacon:
        min_kevin_bacon = kevin_bacon  # 최소 케빈 베이컨 수 업데이트
        min_person = i  # 최소 케빈 베이컨 수를 가진 사람 번호 업데이트

# 결과 출력 (1부터 시작하는 번호로 변환하여 출력)
print(min_person + 1)
