T = int(input())

for tc in range(1,T+1):
    N = int(input()) # N개의 블럭
    N_list = list(map(int, input().split())) # N개 블럭의 각각의 높이
    up_level = 0 # 올라가야 할때 난이도
    down_level = 0 # 내려가야 할때 난이도

    for i in range(N - 1):
        diff = N_list[i+1] - N_list[i] # 현재 블록과 다음 블록의 높이차 계산
        if diff > 0 : # 높이가 증가할 때 (올라가는 값)
            up_level = max(up_level, diff)

        if diff < 0 : # 높이가 감소할 때 (내려가는 값)
            down_level = min(up_level, -diff)

    print(f'#{tc} {up_level} {down_level}')
