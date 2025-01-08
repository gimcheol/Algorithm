# 거스름돈 N이 주어질 때, 2원과 5원 동전으로만 거스름 돈을 거슬러 주어야 한다.
# 단, 동전의 개수가 최소가 되도록 하여야함.
# 거슬러 줄수 없을 경우는 -1을 출력

N = int(input())

cnt = 0

while N > 0:
    if N % 5 == 0:
        cnt += N // 5
        N = 0

    else:
        N -= 2
        cnt +=1

if N >=0:
    print(cnt)

else:
    print(-1)