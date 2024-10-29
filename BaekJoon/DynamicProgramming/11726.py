import sys

n = int(sys.stdin.readline())

dp = [0] * (n+1)

# 점화식 dp[i] = dp[i-1] +dp[i-2] (i >=3)

dp[1] = 1 # 1가지
dp[2] = 2 # 2가지

for i in range(3, n+1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 10007

print(dp[n])
