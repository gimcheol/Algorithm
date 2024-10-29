
n = int(input())

# 5킬로그램 봉지로 최대한 채우기
bag_5 = n // 5

# 남은 무게
remainder = n - bag_5 * 5

# 가능한 경우 탐색
while bag_5 >= 0:
    # 남은 무게가 3의 배수이면 최적해 찾음
    if remainder % 3 == 0:
        bag_3 = remainder // 3
        print(bag_5 + bag_3)
        break
    # 5킬로그램 봉지 하나씩 줄이고 남은 무게 갱신
    bag_5 -= 1
    remainder += 5
# 봉지로 채울 수 없는 경우
else:
    print(-1)
