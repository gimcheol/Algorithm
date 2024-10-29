from itertools import combinations

answer = []

for i in range(9):
    height = int(input())
    answer.append(height)

for a in combinations(answer, 7):
    if sum(a) == 100:
        a = list(a)
        a.sort()
        print(" ".join(a))
        break