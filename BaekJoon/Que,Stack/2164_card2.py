import sys
from collections impor

N = int(sys.stdin.readline())

que = deque()  # 덱 생성
que = deque(range(1, N+1))  # 1부터 N까지의 숫자로 덱 초기화

while len(que) > 1:  # 덱의 길이가 1 초과일 때까지 반복
    que.popleft()  # 맨 앞의 요소 제거
    que.append(que.popleft())  # 맨 앞의 요소를 맨 뒤로 이동하여 추가

print(que.pop())  #  deque에서는 pop(0) 메서드가 제공되지 않습니다.

#