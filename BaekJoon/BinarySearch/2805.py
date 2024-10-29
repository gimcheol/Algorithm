
N, M = map(int, input().split())
tree = list(map(int, input().split()))

# 이분탐색
left = 0
right = max(tree)
height = 0

while left <= right:
    mid = (left + right) // 2 # 절단기 높이

    # 나무를 잘라서 얻는 길이
    wood = 0
    for i in tree:
        if i > mid:
            wood += i - mid

    # 필요한 나무 길이보다 많은 나무를 얻었다면, 더 높게 자를 수 있는지 확인
    if wood >= M:
        height = mid
        left = mid + 1 # 많이 얻었다면 범위를 줄이기 위해 왼쪽 범위를 늘린다.

    else:
        right = mid - 1 # 적게 얻으면 오른쪽범위를 줄인다.

print(height)


