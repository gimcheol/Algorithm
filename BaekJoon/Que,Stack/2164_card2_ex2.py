from collections import deque

N = int(input())  # 예: 7을 입력

d = deque(range(1, N + 1))  # deque([1, 2, 3, 4, 5, 6, 7])

discard = True

while len(d) > 1:
    if discard:
        d.popleft()
        discard = False
    else:
        x = d.popleft()
        d.append(x)
        discard = True

    #print(d)  # 각 단계에서 deque의 상태 출력

print(d[0])  # 마지막 남은 요소 출력
