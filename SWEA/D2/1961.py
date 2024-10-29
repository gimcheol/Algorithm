T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    li = []
    for _ in range(n):
        li.append(list(map(int, input().split())))

    # 회전된 행렬을 저장할 리스트 초기화
    temp90 = [[0] * n for _ in range(n)]
    temp180 = [[0] * n for _ in range(n)]
    temp270 = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            temp90[j][n - i - 1] = li[i][j]  # 90도 회전
            temp180[n - i - 1][n - j - 1] = li[i][j]  # 180도 회전
            temp270[n - j - 1][i] = li[i][j]  # 270도 회전

    # 출력
    print(f"#{test_case}")  # 테스트 케이스 번호 출력
    for i in range(n):
        # 각 회전된 행렬을 공백으로 구분하여 출력
        print(''.join(map(str, temp90[i])), ''.join(map(str, temp180[i])), ''.join(map(str, temp270[i])))
