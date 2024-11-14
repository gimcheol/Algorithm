T = int(input())

for tc in range(1, T+1):

    A, B = map(int, input().split()) # A : 현재시각, B: 경과시간

    after_time = (A + B) % 24

    print(f'#{tc} {after_time}')