T = int(input())

for tc in range(1, T+1):

    N, K = map(int, input().split()) # N : 퍼즐 크기 , K: 단어 길이
    puzzle = [list(map(int, input().split())) for _ in range(N)] # 퍼즐 모양 입력

    cnt = 0 # 들어갈 수 있는 단어 갯수

    # 가로 방향 체크
    for i in range(N):
        length = 0 # 연속된 빈칸의 길이
        for j in range(N):
            if puzzle[i][j] == 1: # 빈칸일 경우
                length += 1
            else: # 벽을 만나면
                if length == K: # 길이가 K인 경우만 단어를 넣을 수 있음
                    cnt += 1
                length = 0 # 길이를 초기화

        if length == K: # 마지막 칸까지 확인
            cnt +=1

    # 세로 방향 체크
    for j in range(N):
        length = 0 # 연속된 빈칸의 길이
        for i in range(N):
            if puzzle[i][j] == 1: # 빈칸일 경우
                length += 1 # 빈칸의 길이를 추가

            else: # 벽을 만나면
                if length == K: # 빈칸의 길이가 K 인경우에만 단어를 집어 넣을 수 있음
                    cnt += 1 # 들어 갈 수 있는 단어개수 추가

                length = 0 # 연속된 빈칸의 길이 확인을 다시 초기화

        if length == K:
            cnt += 1

    print(f'#{tc} {cnt}')
