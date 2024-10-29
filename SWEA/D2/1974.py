# 테스트 케이스 개수 입력 받기
T = int(input())

# 각 테스트 케이스에 대해 처리
for t in range(1, T + 1):
    sudoku = []  # 스도쿠 퍼즐을 저장할 리스트

    # 9x9 스도쿠 퍼즐 입력 받기
    for _ in range(9):
        row = list(map(int, input().split()))  # 각 행 입력받기
        sudoku.append(row)  # 입력된 행을 스도쿠 리스트에 추가

    # 유효성 검사 플래그
    valid = 1  # 스도쿠가 유효할 경우 1로 초기화

    # 1. 행 검사
    for row in sudoku:
        # 숫자가 1~9 사이에 있는지 확인
        for num in row:
            if num < 1 or num > 9:
                valid = 0  # 유효하지 않음
                break  # 잘못된 숫자를 발견했으므로 검사 중단

        # 중복 검사
        if len(set(row)) != 9:
            valid = 0  # 유효하지 않음
            break  # 중복된 숫자를 발견했으므로 검사 중단

    # 2. 열 검사
    for col in range(9):
        column = []  # 현재 열의 숫자를 저장할 리스트
        for row in range(9):
            column.append(sudoku[row][col])  # 각 행에서 현재 열의 숫자를 수집

        # 숫자가 1~9 사이에 있는지 확인
        for num in column:
            if num < 1 or num > 9:
                valid = 0  # 유효하지 않음
                break  # 잘못된 숫자를 발견했으므로 검사 중단

        # 중복 검사
        if len(set(column)) != 9:
            valid = 0  # 유효하지 않음
            break  # 중복된 숫자를 발견했으므로 검사 중단

    # 3. 3x3 구역 검사
    for i in range(0, 9, 3):  # 0, 3, 6: 각 3x3 구역의 시작 행
        for j in range(0, 9, 3):  # 0, 3, 6: 각 3x3 구역의 시작 열
            check = []  # 현재 3x3 구역의 숫자를 저장할 리스트

            # 3x3 구역 내의 숫자를 수집
            for a in range(3):  # 3행
                for b in range(3):  # 3열
                    check.append(sudoku[i + a][j + b])  # 숫자 추가

            # 중복 검사
            if len(set(check)) != 9:  # 중복된 숫자가 있다면
                valid = 0  # 유효하지 않음
                break  # 중복된 숫자를 발견했으므로 검사 중단

    # 결과 출력
    print(f"#{t} {valid}")
