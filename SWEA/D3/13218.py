T = int(input())

for tc in range(1, T+1):

    N = int(input()) # 총 학생의 수

    if N >= 3:
        group_cnt = N // 3

        print(f'#{tc} {group_cnt}')

    elif N < 3:

        print(f'#{tc} 0')