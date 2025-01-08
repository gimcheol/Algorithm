N = int(input()) # 컴퓨터의 수
M = int(input()) # 연결되어있는 컴퓨터 쌍의 수

graph = [[] for _ in range(N)]

for _ in range(M):
    a, b = list(map(int, input().split())) # 연결된 컴퓨터 쌍
    graph[a-1].append(b-1) # a(노드)와 연결된 b(노드) 추가
    graph[b-1].append(a-1) # b(노드)와 연결된 a(노드) 추가

visit = [False] * N

# DFS
def dfs(u):
    visit[u] = True

    for v in graph[u]:
        if not visit[v]:
            dfs(v)

dfs(0)

cnt = 0

for i in range(1, N):
    if visit[i]:
        cnt += 1

print(cnt)