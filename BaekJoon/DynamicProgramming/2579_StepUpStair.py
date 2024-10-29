import sys

input = sys.stdin.readline

N = int(input()) # 계단의 개수

stair = [0] * 301 # 각 계단의 점수
dp = [0] * 301 # 계단의 점수 합한 최댓값 저장

for i in range(1, N+1):

    stair[i] = int(input()) # 계단 점수 입력

# i개의 계단까지 올랐을 때 얻을 수 있는 최대 점수
dp[1] = stair[1]
dp[2] = stair[1] + stair[2]
dp[3] = max(stair[1] + stair[3], stair[2]+stair[3]) # 3개까지만 있을때 마지막을 무조건 밟아야하니까 비교

for i in range(4, N+1):

    dp[i] = max(dp[i-2] + stair[i], dp[i-3] + stair[i-1] + stair[i])

print(dp[N])



