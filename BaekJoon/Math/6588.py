#에라토스테네스의 체
# def sieve_of_eratosthenes(n):
#     # 주어진 범위 내의 모든 수를 대상으로 True로 초기화된 리스트를 생성합니다.
#     prime = [True] * (n+1)
#     prime[0] = prime[1] = False  # 0과 1은 소수가 아닙니다.
#
#     p = 2
#     while p * p <= n:
#         # 현재 숫자(p)가 소수인 경우에만 해당 숫자의 배수들을 소수가 아닌 것으로 표시합니다.
#         if prime[p]:
#             for i in range(p * p, n+1, p):
#                 prime[i] = False
#         p += 1
#
#     # 소수만을 담은 리스트를 생성하여 반환합니다.
#     primes = [i for i in range(2, n+1) if prime[i]]
#     return primes

prime = [True] * 1000001

for i in range(2, int(len(prime) ** 0.5)+1):

    if prime[i]: #소수 인지 아닌지

        for j in range(2 * i,1000001, i):
            prime[j] = False

while 1:

    N = int(input())
    if N ==0:
        break

    for i in range(N-3, 2, -2):
        if prime[i] == True and prime[N-i] == True:
            print(f"{N} = {N-i} + {i}")
            break



