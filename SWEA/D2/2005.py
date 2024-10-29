T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    triangle = []

    # 1부터 N까지 반복 (즉, 1번째 행부터 시작)
    for i in range(1, N + 1):
        row = [1] * i  # i번째 행의 크기는 i로 설정 (1부터 시작)

        # j는 1부터 i-1까지 반복, 처음과 마지막 인덱스는 항상 1이기 때문
        for j in range(1, i - 1):  # j의 범위를 1부터 i-1까지 수정
            row[j] = triangle[i - 2][j - 1] + triangle[i - 2][j]  # 위의 행에서 값을 가져옴

        triangle.append(row)

    print(f"#{tc}")
    for row in triangle:
        print(' '.join(map(str, row)))
