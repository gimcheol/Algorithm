T = int(input())

for tc in range(1,T+1):

    N = int(input())
    N_sum = 0

    for i in range(1, N+1):

        if i % 2 == 1: # 홀수인 경우

            N_sum += i

        else:

            N_sum -= i

    print(f'#{tc} {N_sum}')
