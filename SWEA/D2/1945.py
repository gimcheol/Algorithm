T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # N = 2^a * 3^b * 5^c * 7^d * 11^e
    a, b, c, d, e = 0, 0, 0, 0, 0  # 각 지수를 0으로 초기화

    while N > 1:  # N이 1보다 큰 동안 반복
        if N % 2 == 0:  # 2로 나누어 떨어지면
            a += 1
            N //= 2  # 정수 나누기
        elif N % 3 == 0:  # 3으로 나누어 떨어지면
            b += 1
            N //= 3
        elif N % 5 == 0:  # 5로 나누어 떨어지면
            c += 1
            N //= 5
        elif N % 7 == 0:  # 7로 나누어 떨어지면
            d += 1
            N //= 7
        elif N % 11 == 0:  # 11로 나누어 떨어지면
            e += 1
            N //= 11
        else:
            break  # 더 이상 나누어 떨어지지 않으면 종료

    print(f'#{tc} {a} {b} {c} {d} {e}')  # 결과 출력
