T = int(input())

for i in range(T):
    a, b = map(int, input().split())

    A = int(a//b)
    B = a % b

    print("#{} {:d} {}".format(i + 1, A, B))