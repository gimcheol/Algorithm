import sys

s = set()

m = int(sys.stdin.readline().strip())

for _ in range(m):
    command = sys.stdin.readline().strip().split()

    if command[0] == 'add':
        s.add(int(command[1]))

    elif command[0] == 'remove':
        s.discard(int(command[1]))

    elif command[0] == 'check':
        print(1 if int(command[1]) in s else 0)

    elif command[0] == 'toggle':
        num = int(command[1])

        if num in s:
            s.discard(num)
        else:
            s.add(num)

    elif command[0] == 'all':
        s = set(range(1, 21))
    elif command[0] == 'empty':
        s = set()
