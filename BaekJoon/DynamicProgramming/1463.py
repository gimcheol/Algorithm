N = int(input())

dp = [0]*(N+1) # 최소 연산 횟수를 저장할 리스트 초기화

for i in range(2, N+1):

    # 현재 숫자에서 1을 빼는 경우의 연산 횟수를 저장
    dp[i] = dp[i-1] + 1

    # 숫자가 3과 2로 나누어 떨어질 경우 연산 횟수 업데이트

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

print(dp[N])