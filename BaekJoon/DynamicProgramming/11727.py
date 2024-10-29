import sys

n = int(sys.stdin.readline())

dp = [0] * 1001

# 점화식 dp[i] = dp[i-1] +2 * dp[i-2]

dp[1] = 1 # 1가지
dp[2] = 3 # 3가지

for i in range(3, n+1):
    dp[i] = (dp[i - 1] + 2* dp[i - 2]) % 10007

print(dp[n])
