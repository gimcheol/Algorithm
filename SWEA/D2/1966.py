T = int(input())


for tc in range(1, T+1):

    N = int(input())
    N_list = list(map(int, input().split()))

    answer = sorted(N_list)

    print(f'#{tc}', ' '.join(map(str, answer)))