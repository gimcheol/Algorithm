#16194 카드 구매하기 2
N = int(input())
P = [0] + list(map(int, input().split())) 
dp = [float('inf')] * (N + 1)  # 최소 가격을 저장할 DP 테이블 (무한대로 초기화)

dp[0] = 0  # 카드를 하나도 구매하지 않는 경우의 가격은 0
for i in range(1, N + 1):
    for j in range(1, i + 1):
        dp[i] = min(dp[i], P[j] + dp[i - j])

print(dp[N]) 