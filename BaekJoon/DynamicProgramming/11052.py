N = int(input())  # 카드 묶음의 개수
P = [0] + list(map(int, input().split()))  # 각 카드 묶음의 가격
dp = [0] * (N + 1)  # 최대 가격을 저장할 DP 테이블

# 다이나믹 프로그래밍을 통해 최대 가격 구하기
for i in range(1, N + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], P[j] + dp[i - j])

print(dp[N])  # N개의 카드를 살 때의 최대 가격 출력