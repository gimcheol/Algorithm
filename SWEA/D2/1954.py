# 테스트 케이스 수 T 입력
T = int(input())

# 각 테스트 케이스 처리
for t in range(1, T + 1):
    N = int(input())  # N 크기 입력
    # N*N 크기의 2차원 배열 생성 및 초기화 (모두 0)
    snail = [[0] * N for _ in range(N)]

    # 방향: 오른쪽(0), 아래(1), 왼쪽(2), 위쪽(3)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 이동 방향 정의
    direction_index = 0  # 처음 방향은 오른쪽
    x, y = 0, 0  # 시작 좌표 (0, 0)
    current_number = 1  # 처음 숫자는 1

    # N*N만큼 숫자를 채우기
    for _ in range(N * N):
        # 현재 위치에 숫자를 채움
        snail[x][y] = current_number
        current_number += 1  # 다음 숫자로 증가

        # 다음 위치 계산
        next_x = x + directions[direction_index][0]  # 다음 x 좌표
        next_y = y + directions[direction_index][1]  # 다음 y 좌표

        # 다음 위치가 유효하지 않거나 이미 숫자가 있다면 방향 전환
        if (next_x < 0 or next_x >= N or next_y < 0 or next_y >= N or
                snail[next_x][next_y] != 0):
            direction_index = (direction_index + 1) % 4  # 방향 전환 (시계방향)
            next_x = x + directions[direction_index][0]  # 새 다음 x 좌표
            next_y = y + directions[direction_index][1]  # 새 다음 y 좌표

        # 현재 위치를 다음 위치로 업데이트
        x, y = next_x, next_y

    # 결과 출력
    print(f"#{t}")  # 테스트 케이스 번호 출력
    for row in snail:
        print(" ".join(map(str, row)))  # 배열의 각 행을 공백으로 구분하여 출력
