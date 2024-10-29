N = int(input())

schedule = [] # 리스트로 상담 정보를 저장할 변수

dp = [0] * (N+1)

for _ in range(N):

    T, P = map(int, input().split())
    schedule.append((T, P)) # 리스트에 상담 정보 저장

# 뒤에서부터 거꾸로 DP를 채워나감
for i in range(N-1, -1, -1):
    if i + schedule[i][0] <= N:
        #현재 상담을 선택한 경우와 선택하지 않은 경우 중 최대값 선택
        dp[i] = max(dp[i+1], dp[i + schedule[i][0]] + schedule[i][1])

    else:
        # 현재 상담을 선택 할 수 없는 경우
        dp[i] = dp[i+1]

print(dp[0])