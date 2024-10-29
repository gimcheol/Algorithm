T = int(input())

## dp[i][j] = dp[i-1][j-1]+dp[i][j-1] i>j

for _ in range(T):
    N, M = map(int, input().split())

    dp = [[0] * 30 for _ in range(30)]  # 2차원 리스트로 초기화

    for i in range(30): # 서쪽
        for j in range(30): # 동쪽
            if i == 1:
                dp[i][j] = j # 서쪽에 1개면 동쪽에 있는만큼 놓을 수 있음

            else:
                if i == j:
                    dp[i][j] = 1 ## 양쪽점이 같은 경우 1가지만 놓을 수 있음

                elif i < j:
                    dp[i][j] = dp[i-1][j-1]+ dp[i][j-1] # 점화식

    print(dp[N][M])