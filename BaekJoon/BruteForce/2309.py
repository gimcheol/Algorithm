from itertools import combinations

N = []

for _ in range(9):
    N.append(int(input()))


for i in combinations(N, 7):
    if sum(i) == 100:
        i = list(i)
        i.sort()
        print("\n".join(map(str, i)))
        break