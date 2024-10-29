from collections import deque
import sys

N = int(sys.stdin.readline())

que = deque()
for _ in range(N):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "1":
        que.appendleft(cmd[1])

    elif cmd[0] == "2":
        que.append(cmd[1])

    elif cmd[0] == "3":
        if len(que) > 0:
            print(que.popleft())
        else:
            print("-1")

    elif cmd[0] == "4":
        if len(que) > 0:
            print(que.pop())
        else:
            print("-1")


    elif cmd[0] == "5":
        print(len(que))

    elif cmd[0] == "6":
        if len(que) > 0:
            print("0")
        else:
            print("1")

    elif cmd[0] == "7":
        if len(que) >0:
            print(que[0])
        else:
            print("-1")

    elif cmd[0] == "8":
        if len(que) > 0:
            print(que[-1])
        else:
            print("-1")