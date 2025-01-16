N = int(input())  # 지도 크기 입력
house_map = [list(map(int, input())) for _ in range(N)]  # 지도 입력받기

# 방문한 곳을 기록하기 위한 리스트
visited = [[False] * N for _ in range(N)]

# 방향 벡터 (위, 아래, 왼쪽, 오른쪽)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# DFS 함수 정의
def dfs(x, y):
    visited[x][y] = True  # 현재 위치 방문 표시
    size = 1  # 단지 크기 (현재 집이 있는곳에서 시작하니까 현재 집 포함)

    for i in range(4):  # 상하좌우 탐색
        nx, ny = x + dx[i], y + dy[i]

        # 지도 범위 안에 있고, 집이 있으며, 방문하지 않은 곳
        if 0 <= nx < N and 0 <= ny < N and house_map[nx][ny] == 1 and not visited[nx][ny]:
            size += dfs(nx, ny)  # 연결된 집 크기 더하기
    return size

# 단지 정보 저장
complex_sizes = []

# 지도 전체를 탐색하며 단지 찾기
for i in range(N):
    for j in range(N):
        if house_map[i][j] == 1 and not visited[i][j]:  # 새 단지를 발견한 경우
            complex_sizes.append(dfs(i, j))

# 결과 출력
print(len(complex_sizes))  # 단지 수
for size in sorted(complex_sizes):  # 단지 크기 오름차순 출력
    print(size)
