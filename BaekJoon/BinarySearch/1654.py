K, N = map(int, input().split())
lan = [int(input()) for _ in range(K)]

left = 1  # 랜선의 최소 길이는 1입니다.
right = max(lan)

while left <= right:
    middle = (left + right) // 2
    lancnt = 0

    for length in lan:
        lancnt += length // middle  # middle 길이로 잘랐을 때 나오는 랜선 개수를 누적합니다.

    if lancnt >= N:
        left = middle + 1
    else:
        right = middle - 1

print(right)
