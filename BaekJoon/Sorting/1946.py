import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    N = int(input())
    candidates = []

    for j in range(N):
        grade1, grade2 = map(int, input().split())
        candidates.append((grade1, grade2))

    # (grade1, grade2) 첫번째 점수 기준 정렬
    candidates.sort()

    top_ranking = N # 최고순위
    count = 0 # 합격자

    for k in range(N):
        if candidates[k][1] < top_ranking: #현재 보는 후보자의 면접점수 비교
            count += 1
            top_ranking = candidates[k][1]

    print(count)
