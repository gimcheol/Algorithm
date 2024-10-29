# 테스트 케이스 수 입력 받기
T = int(input())

# 각 테스트 케이스 처리
for tc in range(1, T + 1):
    # 리스트 A와 B의 길이 입력 받기
    N, M = map(int, input().split())

    # 숫자열 A와 B 입력 받기
    A = list(map(int, input().split()))  # 숫자열 Ai : (i + 1 ~ N)
    B = list(map(int, input().split()))  # 숫자열 Bj : (j + 1 ~ M)

    max_sum = 0  # 최댓값 초기화

    # A가 B보다 길 경우 두 리스트의 순서를 바꿈
    if len(A) > len(B):
        A, B = B, A

    # 리스트의 새로운 길이 갱신
    N = len(A)
    M = len(B)

    # B에서 A가 시작할 수 있는 모든 위치에 대해 반복
    for i in range(M - N + 1):
        current_sum = 0  # 현재 합 초기화

        # A의 각 요소와 B의 현재 위치 요소를 곱하여 합산
        for j in range(N):
            current_sum += A[j] * B[i + j]  # B[i + j]는 A가 현재 위치에서 마주보는 값

        # 최댓값 갱신
        max_sum = max(max_sum, current_sum)

    # 결과 출력 (테스트 케이스 번호와 최댓값)
    print(f'#{tc} {max_sum}')
