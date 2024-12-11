from collections import deque
N, M = map(int, input().split()) # 가로 N, 세로 M의 전쟁터

graph = [[] for _ in range(M)] # 전쟁터 지도
visited = [[False] * N for _ in range(M)] # 방문 여부를 기록할 배열

# 방향 벡터 2차원 배열에서 이동 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 각 군의 전투력
white_score = 0
blue_score = 0

for i in range(M):
    for j in range(M):
        if not visited[i][j]: # 방문하지 않은 병사를 찾음
            team = graph[i][j] # 현재 병사의 팀 ('W' 또는 'B')
            queue = deque([(i, j)])
            visited[i][j] = True
            cnt = 0 # 연결된 병사의 수

            # BFS 수행
            while queue:
                x, y = queue.popleft()
                cnt += 1 # 병사 한명 추가

                for k in range(4): # 4방향 탐색
                    nx,

