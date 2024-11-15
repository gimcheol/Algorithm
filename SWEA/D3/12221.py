TC = int(input())

for tc in range(1, TC+1):

    A, B = map(int, input().split())

    if A<10 and B<10:

        print(f'#{tc} {A*B}')

    else:

        print(f'#{tc} -1')