T = int(input())

for t in range(1, T+1):

    N, M = map(int, input().split())

    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))

    max_flies = 0

    for i in range(N - M + 1):
        for j in range(N - M + 1):

            flies = 0
            for x in range(i, i + M):
                for y in range(j, j + M):
                    flies += grid[x][y]


            if flies > max_flies:
                max_flies = flies

    print(f"#{t} {max_flies}")
