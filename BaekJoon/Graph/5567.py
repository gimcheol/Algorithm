N = int(input())  # 동기의 수 (노드의 수)
m = int(input())  # 친구 관계(간선)의 수

# 인접 리스트 초기화: 각 동기(노드)에 대해 빈 리스트 생성
adj = [[] for _ in range(N)]

# m개의 친구 관계를 입력 받아 인접 리스트 adj에 추가
for _ in range(m):
    a, b = list(map(int, input().split()))  # 서로 친구인 동기 관계
    adj[a - 1].append(b - 1)  # a번 동기와 b번 동기가 친구 관계이므로 각각 리스트에 추가
    adj[b - 1].append(a - 1)  # 위와 반대로도 추가 (무방향 그래프)

# 1촌 친구를 표시할 배열 초기화 (0으로 채운 N 크기의 리스트)
friend = [0] * N

# 1. 0번 동기의 1촌 친구들을 friend 배열에 표시
for i in adj[0]:  # 0번 동기와 직접 친구인 동기들 탐색
    friend[i] = 1  # 해당 동기는 1촌 친구이므로 friend 배열에서 해당 인덱스를 1로 설정

# 2촌 친구를 표시할 배열 초기화
friend2 = [0] * N

# 2. 1촌 친구들의 친구(2촌 친구)를 friend2 배열에 표시
for i in range(N):
    if friend[i] == 0:  # 만약 i번 동기가 1촌 친구가 아니면 스킵
        continue

    for j in adj[i]:  # i번 동기의 친구들 탐색
        if j != 0 and friend[j] == 0:  # j번 동기가 0번 동기가 아니고, 아직 1촌 친구로 표시되지 않았다면
            friend2[j] = 1  # j번 동기는 2촌 친구이므로 friend2 배열에서 해당 인덱스를 1로 설정

# 1촌 친구의 수와 2촌 친구의 수를 더한 값을 출력
print(sum(friend) + sum(friend2))
