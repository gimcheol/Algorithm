import sys

T = int(sys.stdin.readline())

stack = []

for i in range(T):
    N = int(sys.stdin.readline().strip())

    if N > 0:
        stack.append(N)
    elif N == 0:
        if stack: # 스택이 비어있을때는 실행되지 않음
            stack.pop()

answer = sum(stack)

print(answer)