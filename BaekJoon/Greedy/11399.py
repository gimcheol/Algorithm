# 변수 사용방식
N = int(input()) # 돈을 인출하는 사람 수
P = list(map(int, input().split())) # 돈을 인출하는데 걸리는 시간
P.sort()

answer = 0 # 총 대기시간을 저장할 변수
current_time = 0 # 현재까지 걸린 대기시간을 저장할 변수 기다리는 시간에 더해주는건데 왜 필요없다고 없앴냐?

for time in P:
    current_time +=time
    answer += current_time

print(answer)

# 배열 사용 방식
# N = int(input()) # 돈을 인출하는 사람 수
# P = list(map(int, input().split())) # 돈을 인출하는데 걸리는 시간
#
# P = sorted(P)
#
# waitting = [0] * N
# waitting[0] = P[0]
#
# for i in range(1, N):
#     waitting[i] = waitting[i - 1] + P[i]
#
# print(sum(waitting))