from collections import deque

# 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 함수: 한 덩어리의 빙산을 탐색
def bfs(x, y):
    queue = deque([(x, y)])  # 큐에 시작점을 넣고
    visited[x][y] = True  # 시작점을 방문 처리
    while queue:
        cx, cy = queue.popleft()  # 큐에서 하나씩 빼서
        # 상하좌우 탐색
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            # 유효한 범위 내에서 방문하지 않았고 얼음이 있는 곳이라면
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and ice[nx][ny] > 0:
                visited[nx][ny] = True  # 방문 처리
                queue.append((nx, ny))  # 큐에 새로운 위치를 추가

# 얼음 녹이기 함수
def melt():
    global ice
    temp_ice = [[0] * M for _ in range(N)]  # 임시 배열에 새로운 얼음 상태 저장
    for i in range(N):
        for j in range(M):
            if ice[i][j] > 0:
                melt_amount = 0
                # 상하좌우를 확인하여 바다와 인접한 개수만큼 녹음
                for k in range(4):
                    ni, nj = i + dx[k], j + dy[k]
                    if 0 <= ni < N and 0 <= nj < M and ice[ni][nj] == 0:
                        melt_amount += 1
                # 얼음이 녹은 만큼 새로 갱신
                temp_ice[i][j] = max(ice[i][j] - melt_amount, 0)
    ice = temp_ice  # 갱신된 얼음 상태로 바꿔줌

# 입력 받기
N, M = map(int, input().split())  # 맵 크기 N x M
ice = [list(map(int, input().split())) for _ in range(N)]  # 얼음 맵 입력

# 년도 계산
years = 0

# 빙산이 모두 녹거나 두 덩어리 이상으로 분리될 때까지 반복
while True:
    # 빙산 덩어리 개수 확인 (DFS 또는 BFS로 탐색)
    visited = [[False] * M for _ in range(N)]  # 방문 처리 배열
    count = 0  # 빙산 덩어리 개수
    for i in range(N):
        for j in range(M):
            if ice[i][j] > 0 and not visited[i][j]:  # 얼음이 있고, 방문하지 않았다면
                bfs(i, j)  # BFS로 덩어리 탐색
                count += 1  # 덩어리 수 증가

    # 빙산이 두 덩어리 이상으로 분리되었으면 종료
    if count >= 2:
        print(years)  # 걸린 년수 출력
        break

    # 빙산이 모두 녹았다면 종료
    if count == 0:
        print(0)  # 모든 빙산이 녹았으므로 0 출력
        break

    # 빙산 녹이기
    melt()
    years += 1  # 1년 추가
