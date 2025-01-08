import sys
sys.setrecursionlimit(10**6)

N = int(input())

adj = [[] for _ in range(N)]

for _ in range(N-1):
    a, b = list(map(int, input().split())) # 연결된 두 정점
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)

visit = [False] * N
parenst = [-1] * N

# DFS
def dfs(u):
    visit[u] = True

    for v in adj[u]:
        if not visit[v]:
            parenst[v] = u
            dfs(v)

# 첫번째부터 시작
dfs(0)

for i in range(1, N):
    print(parenst[i] + 1)