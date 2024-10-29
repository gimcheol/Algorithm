N = int(input()) # 게임 레벨의 수
L = [0] * N

for i in range(N):
    L[i] = int(input())

count = 0

for i in range(N - 2, -1, -1):
    if L[i] >= L[i + 1]:
        count += L[i] - (L[i + 1] - 1) # L[i] - L[i+1]을 하면 크기가 같아지니까 추가로 -1을 더해줌
        L[i] = L[i + 1] - 1

print(count)