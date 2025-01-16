from collections import deque

N = int(input()) # 사람 수
a, b = map(int, input().split()) # 촌수를 계산해야 하는 두 사람의 번호
m = int(input()) # 부모 자식들 간의 관계의 개수

# 가족 관계를 저장할 인접 리스트
famliy = [[] for _ in range(N)]

for _ in range(m):
    x, y = map(int, input().split())
    famliy[x-1].append(y-1)
    famliy[y-1].append(x-1)

# 방문 여부 리스트
visit = [False] * N

# BFS
def bfs(start, target):
    queue = deque([start]) # 시작 노드를 큐에 추가
    visit[start] = True # 시작 노드 방문처리
    distance = [0] * N # 촌수 저장 리스트

    while queue:
        current = queue.popleft() # 큐에서 현재 노드 꺼내기

        # 목표 노드에 도달하면 촌수 반환
        if current == target:
            return distance[current]

        # 현재 노드와 연결된 노드 탐색
        for neighbor in famliy[current]:
            if not visit[neighbor]: # 방문 안됐으면
                queue.append(neighbor) # 큐에 삽입하고
                visit[neighbor] = True  # 방문처리 해줌
                distance[neighbor] = distance[current] + 1 # 촌수 갱신

    # 목표 노드를 찾지 못한 경우
    return -1

result = bfs(a - 1, b - 1)
print(result)