# 입력: N(가로등의 수), K(확인할 구간의 길이), B(고장난 가로등의 수)
N, K, B = list(map(int, input().split()))

# check 배열을 만들어 모든 가로등의 상태를 0으로 초기화
check = [0] * N

# 고장난 가로등의 위치를 입력받아 check 배열에 표시
for _ in range(B):
    broken_light = int(input())  # 고장난 가로등의 위치 입력
    check[broken_light - 1] = 1  # 고장난 가로등의 위치를 1로 표시 (1-based index를 0-based index로 변환)

# 누적 합 배열을 생성하여 초기화
psum = [0] * N
# 첫 번째 가로등의 고장 여부를 누적 합 배열에 반영
psum[0] = check[0]

# 누적 합 배열 계산: psum[i]는 0부터 i까지의 고장난 가로등 수를 나타냄
for i in range(1, N):
    psum[i] = psum[i - 1] + check[i]

# 필요한 수리 가로등 수를 저장할 리스트
need = []
# 각 구간을 확인하여 고장난 가로등의 수를 계산
for i in range(0, N - K + 1):
    if i == 0:
        # 첫 번째 구간의 고장난 가로등 수는 psum[i + K - 1]로 계산
        num = psum[i + K - 1]
    else:
        # 그 이후 구간의 고장난 가로등 수는 psum[i + K - 1] - psum[i - 1]로 계산
        num = psum[i + K - 1] - psum[i - 1]
    # 각 구간에서의 고장난 가로등 수를 리스트에 추가
    need.append(num)

# 최소 수리 필요한 가로등 수를 출력
print(min(need))
