import sys

T = int(sys.stdin.readline())
stack = [] ## 스택을 밖에다 초기화 해줘야한다. 그래야 여러개의 명령을 한 스택이 처리하니까.
for i in range(T):

    N = sys.stdin.readline().split()

    if N[0] == "1":
        stack.append(N[1])

    elif N[0] == "2":
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)

    elif N[0] == "3":
        print(len(stack))

    elif N[0] == "4":
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif N[0] == "5":
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)