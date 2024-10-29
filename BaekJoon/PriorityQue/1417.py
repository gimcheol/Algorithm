from queue import PriorityQueue

N = int(input()) # 출마후보 수
vote = [0] * N # 출마 후보의 득표 수
pq = PriorityQueue()
cnt = 0

for i in range(N):
    vote[i] = int(input()) # 득표 수

for i in range(1, N):
    pq.put(-vote[i])

if N == 1:
    print(0)

else:
    # 1표씩 매수
    while True:
        max_value = -pq.get()
        if max_value < vote[0]:
            break

        max_value -= 1
        vote[0] +=1
        cnt +=1
        pq.put(-max_value)

    print(cnt)