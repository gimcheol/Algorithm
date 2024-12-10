from collections import deque

# 입력 받기
n, m, v = map(int, input().split())  # 정점의 개수 n, 간선의 개수 m, 시작 정점 v
# graph: 각 정점에 연결된 다른 정점들의 리스트를 저장하는 인접 리스트
graph = [[] for _ in range(n+1)]  # 1번부터 n번까지의 정점을 저장, 0번은 사용하지 않음

# 간선 정보 입력 받기
for _ in range(m):
    a, b = map(int, input().split())  # 간선 a-b 입력 받기
    graph[a].append(b)  # a번 정점에 b번 정점 연결
    graph[b].append(a)  # b번 정점에 a번 정점 연결 (무방향 그래프)

# 각 정점의 연결 정보를 오름차순으로 정렬
# 오름차순 정렬 이유: 가독성 향상 및 탐색 순서 일관성 유지
for i in graph:
    i.sort()  # 각 정점에 연결된 노드들을 오름차순으로 정렬

# DFS (깊이 우선 탐색) 구현
visited = [False] * (n+1)  # 방문 여부를 확인하는 리스트, 1번부터 n번까지의 정점에 대해 방문 여부 기록
dfs_result = []  # DFS 결과를 저장할 리스트

# DFS는 스택을 사용하여 구현 (후입선출 LIFO 방식)
stack = [v]  # 시작 정점 v를 스택에 넣음
while stack:
    current = stack.pop()  # 스택에서 마지막으로 넣은 정점을 꺼냄
    if not visited[current]:  # 만약 아직 방문하지 않았다면
        visited[current] = True  # 방문 처리
        dfs_result.append(current)  # 탐색한 정점 추가
        # 현재 정점의 인접 노드를 뒤에서부터 스택에 추가 (reverse로 뒤집어 넣음)
        for i in reversed(graph[current]):  # 스택은 후입선출이므로 뒤에서부터 추가하여 순서대로 탐색
            if not visited[i]:  # 방문하지 않은 노드만
                stack.append(i)  # 스택에 추가

# BFS (너비 우선 탐색) 구현
visited = [False] * (n+1)  # 방문 여부를 확인하는 리스트 초기화
bfs_result = []  # BFS 결과를 저장할 리스트

# BFS는 큐를 사용하여 구현 (선입선출 FIFO 방식)
queue = deque([v])  # 시작 정점 v를 큐에 넣음
visited[v] = True  # 시작 정점 방문 처리
while queue:
    current = queue.popleft()  # 큐에서 가장 먼저 들어온 정점을 꺼냄
    bfs_result.append(current)  # 탐색한 정점 추가
    for i in graph[current]:  # 현재 정점과 연결된 모든 정점을 탐색
        if not visited[i]:  # 방문하지 않은 노드만
            visited[i] = True  # 방문 처리
            queue.append(i)  # 큐에 추가

# 결과 출력
# *bfs_result는 리스트를 언팩하여 각 요소를 공백으로 구분해서 출력
print(*dfs_result)  # DFS 탐색 결과 출력
print(*bfs_result)  # BFS 탐색 결과 출력
