from collections import deque

# 입력 받기
N, M = map(int, input().split())

# 미로 입력받기
maze = [list(map(int, input())) for _ in range(N)]

# 방향 벡터 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 함수
def bfs(x, y):
    queue = deque([(x, y)])  # 큐에 시작점 추가

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 미로 범위 내에 있고, 이동할 수 있는 칸(1)인 경우
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1  # 현재 위치에서 1을 더한 값 저장
                queue.append((nx, ny))  # 큐에 새 위치 추가

    return maze[N-1][M-1]  # 최종 도착점의 값이 최단 거리

# 결과 출력
print(bfs(0, 0))
