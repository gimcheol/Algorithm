from collections import deque

N = int(input())  # 지역을 나타내는 2차원 배열의 열과 행의 개수

graph = []

for i in range(N):
    spot = list(map(int, input().split()))
    graph.append(spot)  # 각 행을 graph에 추가

max_value = max(map(max, graph))

# 방문 여부 배열
visit = [[False] * N for _ in range(N)]

# 4방향 이동을 위한 방향 설정 (위, 아래, 왼쪽, 오른쪽)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y, height):
    queue = deque([(x, y)])
    visit[x][y] = True

    while queue:
        cx, cy = queue.popleft()

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny] and graph[nx][ny] > height:
                visit[nx][ny] = True
                queue.append((nx, ny))

max_safe_areas = 0  # 최대 안전 구역의 개수

for height in range(max_value + 1):  # 모든 높이에 대해 탐색
    visit = [[False] * N for _ in range(N)]  # 방문여부 초기화
    safe_areas = 0

    for i in range(N):
        for j in range(N):
            if not visit[i][j] and graph[i][j] > height:  # 방문되지 않고, 물에 잠기지 않은 경우
                bfs(i, j, height)
                safe_areas += 1  # 안전구역 개수 증가

    max_safe_areas = max(max_safe_areas, safe_areas)  # 안전구역의 최대값 갱신

print(max_safe_areas)