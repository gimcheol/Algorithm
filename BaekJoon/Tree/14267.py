N, M = list(map(int, input().split()))
parent = list(map(int, input().split()))  # 부모 노드의 번호 (1~N)
good = [0] * N  # 각 직원이 독자적으로 받은 칭찬 수치
total_good = [0] * N  # 각 직원이 받은 총 칭찬 수치

# 부모 노드 인덱스 조정 (1-based index -> 0-based index)
for i in range(1, N):
    parent[i] -= 1

# 각 직원이 받은 칭찬 점수 누적
for _ in range(M):
    id, score = list(map(int, input().split()))  # 칭찬을 받은 직원 번호, 칭찬의 수치
    good[id - 1] += score

# 총 칭찬 점수 계산
for i in range(1, N):
    total_good[i] = total_good[parent[i]] + good[i]

# 루트 노드의 총 칭찬 수치 추가 (자기 자신이 받은 칭찬)
total_good[0] = good[0]

# 결과 출력
print(' '.join(map(str, total_good)))
