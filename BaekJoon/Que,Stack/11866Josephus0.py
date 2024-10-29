from collections import deque

N, K = map(int, input().split()) # (7,3) 총 7명, 3번째 삭제

queue = deque([i for i in range(1, N+1)])
result = []

while queue:
    for _ in range(K - 1):
        queue.append(queue.popleft())
    result.append(str(queue.popleft()))

print("<", ', '.join(result), ">", sep="")
