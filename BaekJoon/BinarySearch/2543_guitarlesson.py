N, M = map(int, input().split())
record = list(map(int, input().split()))


#이분 탐색
left = max(record)
right = sum(record)
answer = 0
while left <= right:
    middle = (left + right) // 2 # 임시 블루레이 용량

    blueray_num = 1
    remain = middle # 1번 블루레이에 남아있는 용량

    for i in range(N):
        if remain < record[i]:
            blueray_num += 1
            remain = middle

        remain -= record[i]

    if blueray_num <= M:
        answer= middle
        right = middle - 1 # [left, middle -1]

    else:
        left = middle + 1 # [middle+1 , right]

print(answer)