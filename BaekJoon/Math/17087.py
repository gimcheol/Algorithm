# 유클리드 호제법
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

# N, S 값을 입력으로 받음
N, S = map(int, input().split())

# 거리 값 리스트를 입력으로 받아 각 요소의 S와의 절대값 차이를 계산하여 리스트에 저장
N_distance = list(map(int, input().split()))
for i in range(N):
    N_distance[i] = abs(S - N_distance[i])

# 초기값 설정
answer = N_distance[0]

# 최대공약수 계산
for j in range(1, N):
    answer = gcd(answer, N_distance[j])

# 결과 출력
print(answer)
