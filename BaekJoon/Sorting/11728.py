# 첫 줄에서 두 정수 N과 M을 입력받습니다.
N, M = map(int, input().split())

# 두 번째 줄에서 N개의 정수를 입력받아 리스트 A로 만듭니다.
A = list(map(int, input().split()))

# 세 번째 줄에서 M개의 정수를 입력받아 리스트 B로 만듭니다.
B = list(map(int, input().split()))

# 병합할 결과 리스트 C를 초기화합니다.
C = []

# 리스트 A와 B를 병합하기 위한 초기 위치를 설정합니다.
pos1 = 0
pos2 = 0

# 두 리스트를 병합합니다.
while pos1 < N and pos2 < M:
    candidate1 = A[pos1]
    candidate2 = B[pos2]

    if candidate1 < candidate2:
        C.append(candidate1)
        pos1 += 1
    else:
        C.append(candidate2)
        pos2 += 1

# 리스트 A에 남은 요소가 있다면 리스트 C에 추가합니다.
if pos1 != N:
    C.extend(A[pos1:N])

# 리스트 B에 남은 요소가 있다면 리스트 C에 추가합니다.
if pos2 != M:
    C.extend(B[pos2:M])

# 리스트 C의 요소들을 공백으로 구분하여 출력합니다.
for i in range(N + M):
    print(C[i], end=" ")

print()  # 마지막에 개행 문자 추가
