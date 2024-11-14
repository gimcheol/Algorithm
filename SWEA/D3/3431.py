T = int(input())

for tc in range(1, T+1):
    L, U, X = list(map(int, input().split()))

    if X > U:
        print(f"#{tc} -1")  # 운동 시간이 최대 시간 초과

    elif X < L:
        additional_exercise = L - X  # 부족한 운동 시간
        print(f"#{tc} {additional_exercise}")

    else:
        print(f"#{tc} 0")  # 추가 운동이 필요 없음
