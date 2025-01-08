# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하시오
# 1~N까지 자연수 중에서 중복없이 M개를 고른 수열 (조합)
# 고른 수열은 오름차순이어야함.

from itertools import combinations

N, M = map(int, input().split())

list = []

for i in combinations(range(1, N+1), M):
    list.append(i)

for i in list:
    print(" ".join(map(str, i)))