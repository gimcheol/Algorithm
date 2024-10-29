N = int(input())
parent = list(map(int, input().split()))
R = int(input())

# 루트 노드 찾기
for i in range(N):
    if parent[i] == -1:
        root = i
        break

# 사라진 노드들 판별
black = [0] * N
for i in range(N):
    u = i
    while True:
        if u == R:  # 삭제된 노드 R에 도달한 경우
            black[i] = 1
            break
        if u == root:  # 루트 노드에 도달한 경우
            break
        u = parent[u]

# 자식이 있는 노드들 색칠
red = [0] * N
for i in range(N):
    if black[i] == 1:
        continue
    if i == root:
        continue
    red[parent[i]] = 1  # 부모 노드에 자식이 있음을 표시

# 리프 노드 수 카운트
count = 0
for i in range(N):
    if black[i] == 1 or red[i] == 1:  # 삭제된 노드거나 자식이 있는 노드는 제외
        continue
    count += 1

print(count)
