M, N, H = list(map(int, input().split())) # 상자 가로크기, 상자 세로크기, 상자 높이(쌓아올려지는 상자의 수)
adj = [] # 토마토 그래프

for _ in range(H):
    layer = []

    for _ in range(N)
        row = list(map(int, input().split()))
        layer.append(row)
    adj.append(layer) # 각 층을 추가
# 상, 하, 좌, 우, 위, 아래
dz = [0, 0, 0, 0, -1, 1]
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]


visit = [[[False] * M for _ in range(N)] for _ in range(H)]
# dfs
def dfs(z, x, y):
    # 현재 위치 방문처리
    visit[z][x][y] = True

    # 6방향 탐색
    for i in range(6):
        nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]

        # 범위 체크와 방문여부 확인
        if 0 <= nz < H and 0<= nx < N and 0 <= ny < M:
            if not visit[nz][nx][ny] and adj[nz][nx][ny] == 0: # 방문이 안됐고, 익지 않은 토마토라면
                visit[nz][nx][ny] = True # 방문처리
                adj[nz][nx][ny] = adj[z][x][y] + 1
                dfs(nz, nx, ny)

# 모든 토마토가 익었는지 확인 및 최소 날짜 계산
def solve():
    cnt = 0
    for z in range(H):
        for x in range(N):
            for y in range(M):
                if adj[z][x][y] == 1 and not visit[z][x][y]:
                    dfs()
                if adj[z][x][y] == 0:
                    cnt += 1
