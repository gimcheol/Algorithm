N = int(input()) # 컴퓨터의 수
M = int(input()) # 연결되어 있는 컴퓨터 쌍의 수

adj = [[] for _ in range(N)]    # 인접 리스트 :N 개의 빈 배열 ( [ [], [], ...[] ] ), adj[i] : 컴퓨터 i 가 연결된 컴퓨터 목록([a, b])

for _ in range(M):
    a, b = list(map(int, input().split())) # 서로 연결된 컴퓨터 번호
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)

check = [0] * N
check[0] = 1

while True:
    new = False

    for i in range(N):
        if check[i] == 0:
            continue
        else:
            for j in adj[i]:
                if check[j] == 0:
                    check[j] = 1
                    new = True

    if new == False:
        continue
    break

cnt = 0
for i in range(1, N):
    if check[i] == 1:
        cnt += 1

print(cnt)

