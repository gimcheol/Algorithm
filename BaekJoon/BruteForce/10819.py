from itertools import permutations

N = int(input())
A = list(map(int, input().split()))
max_diff_sum = 0

for i in permutations(A, N):
    diff_sum = 0

    for j in range(N-1):
        diff_sum += abs(i[j] - i[j + 1])

    max_diff_sum = max(max_diff_sum, diff_sum)

print(max_diff_sum)