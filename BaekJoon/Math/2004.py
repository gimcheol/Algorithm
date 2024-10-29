N, M = map(int, input().split())

def count2(N):
    num2 = 0

    while N>0:
        N //= 2 # N = N//2
        num2+= N

    return num2

def count5(N):
    num5 = 0

    while N >0:
        N //= 5 # N = N//2
        num5 += N

    return num5

# 각각의 팩토리얼 계산에서 중복되는 소인수 2의 개수를 제거
sum2 = count2(N) - count2(M) - count2(N-M)
sum5 = count5(N) - count5(M) - count5(N-M)

print(min(sum2, sum5))