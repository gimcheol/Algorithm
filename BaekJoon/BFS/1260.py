from collections import deque

# 입력 처리
N, M, V = map(int, input().split())  # N: 정점의 개수, M: 간선의 개수, V: 시작 정점 번호
adj = [[] for _ in range(N)]  # 각 정점의 인접 리스트 생성

# 간선 정보 입력
for _ in range(M):
    a, b = map(int, input().split())  # 연결된 두 정점 입력
    adj[a - 1].append(b - 1)  # 양방향 그래프: a에서 b로
    adj[b - 1].append(a - 1)  # b에서 a로도 연결

# BFS 함수 정의
def bfs(start):
    visit = [False] * N  # 방문 여부를 확인하는 리스트 초기화
    queue = deque([start])  # BFS에서 사용할 큐 초기화 (시작 정점 삽입)
    visit[start] = True  # 시작 정점을 방문 처리

    while queue:  # 큐가 빌 때까지 반복
        u = queue.popleft()  # 큐에서 노드 하나를 꺼냄
        print(u + 1, end=" ")  # 방문한 노드 출력 (1부터 시작하도록 출력 조정)

        for v in sorted(adj[u]):  # 현재 노드와 연결된 인접 노드 탐색 (오름차순 정렬)
            if not visit[v]:  # 아직 방문하지 않은 노드라면
                queue.append(v)  # 큐에 추가
                visit[v] = True  # 방문 처리

# DFS 함수 정의 (재귀 방식)
def dfs(u, visit):
    visit[u] = True  # 현재 노드 방문 처리
    print(u + 1, end=" ")  # 방문한 노드 출력 (1부터 시작하도록 출력 조정)

    for v in sorted(adj[u]):  # 현재 노드와 연결된 인접 노드 탐색 (오름차순 정렬)
        if not visit[v]:  # 아직 방문하지 않은 노드라면
            dfs(v, visit)  # 재귀 호출로 다음 노드 방문

# DFS 탐색 실행
visit = [False] * N  # DFS용 방문 리스트 초기화
dfs(V - 1, visit)  # 시작 정점 V에서 탐색 시작 (0-based로 변환)
print()  # 줄 바꿈

# BFS 탐색 실행
bfs(V - 1)  # 시작 정점 V에서 탐색 시작 (0-based로 변환)
