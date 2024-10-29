N = int(input())  # 패턴의 반복 횟수 (Pn에서 O의 반복 횟수)
M = int(input())  # 주어진 문자열 S의 길이
S = input()  # 문자열 S

mod = int(1e9 + 7)  # 모듈러 값
po = [0] * M  # 31의 제곱수를 저장할 배열
po[0] = 1

# 31의 제곱수 배열을 미리 계산
for i in range(1, M):
    po[i] = po[i - 1] * 31 % mod

# Pn 패턴을 생성 (Pn = IOIOI...OI, O가 N개 포함)
Pn = 'I' + 'OI' * N
K = len(Pn)  # 패턴의 길이

# Pn의 해시 값 계산
Pn_hash = 0
for i in range(K):
    Pn_hash *= 31
    Pn_hash %= mod
    Pn_hash += ord(Pn[i]) - ord('A') + 1
    Pn_hash %= mod

# 첫 번째 부분 문자열의 해시 값 계산
S_hash = 0
for i in range(K):
    S_hash *= 31
    S_hash %= mod
    S_hash += ord(S[i]) - ord('A') + 1
    S_hash %= mod

count = 0  # 패턴을 찾은 횟수

# 슬라이딩 윈도우로 문자열을 순회하며 해시 값을 갱신하고 비교
for i in range(M - K + 1):
    if S_hash == Pn_hash:
        count += 1

    # S_hash 갱신 (슬라이딩 윈도우)
    if i + K < M:
        largest = ord(S[i]) - ord('A') + 1
        S_hash += mod - largest * po[K - 1] % mod
        S_hash %= mod
        S_hash *= 31
        S_hash %= mod
        S_hash += ord(S[i + K]) - ord('A') + 1
        S_hash %= mod

print(count)
