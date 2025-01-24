import sys
sys.setrecursionlimit(10**6)


N = int(input()) # 지역을 나타내는 2차원 배열의 열과 행의 개수

graph = []

for i in range(N):
    spot = list(map(int, input().split()))
    graph.append(spot) # 각 행을 graph에 추가

max_value = max(map(max, graph))

visit = [[False] * N for _ in range(N)] # 2차원 방문여부 배열

def dfs(x, y, height):
    if x < 0 or x >= N or y < 0 or y >= N or visit[x][y] or graph[x][y] <= height:
        return

    visit[x][y] = True

    # 상하좌우 이동
    dfs(x - 1, y, height)
    dfs(x + 1, y, height)
    dfs(x, y - 1, height)
    dfs(x, y + 1, height)

max_safe_areas = 0 # 최대 안전 구역의 개수

for height in range(max_value + 1): # 모든 높이에 대해 탐색
    visit = [[False] * N for _ in range(N)] # 방문여부 초기화
    safe_areas = 0

    for i in range(N):
        for j in range(N):
            if not visit[i][j] and graph[i][j] > height: # 방문되지 않고, 물에 잠기지 않은 경우
                dfs(i, j, height)
                safe_areas += 1 # 안전구역 개수증가


    max_safe_areas = max(max_safe_areas, safe_areas) # 안전구역의 최대값 갱신

print(max_safe_areas)