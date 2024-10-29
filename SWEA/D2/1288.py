T = int(input())

for tc in range(1, T+1):

    N = int(input())
    cnt = 1
    answer = []

    while True:
        product = N * cnt
        for i in str(product):
            if int(i) not in answer:
                answer.append(int(i))

        if len(answer) == 10:
            break

        cnt += 1

    print(f'#{tc} {cnt*N}')