import sys

input = sys.stdin.readline

T = int(input())
MAX_N = 1000000
MOD = 1000000009

# dp 리스트를 계산
dp = [0] * (MAX_N + 1)
dp[1], dp[2], dp[3] = 1, 2, 4
for i in range(4, MAX_N+1):
    dp[i] = (dp[i-3] + dp[i-2] + dp[i-1]) % MOD

# 각 테스트 케이스에 대해 결과 출력
for _ in range(T):
    N = int(input())
    print(dp[N])
