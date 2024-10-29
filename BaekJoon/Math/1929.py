#입력이 공백으로 구분되어 두 개의 정수를 받아야 한다면,
#.split() 함수를 사용

M, N = map(int, input().split())

for i in range(M, N+1):

    if i == 1: # 1은 소수가 아님
        continue

    prime_number = True

    for j in range(2, int(i**0.5)+1): # 에라토스테네스의 체

        if i % j == 0:
            prime_number = False
            break

    if prime_number:
        print(i)
