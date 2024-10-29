import sys
input = sys.stdin.readline

N = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

# 최소 비용 계산
total_cost = 0
min_price = price[0] # 주유소중 가장 저렴한 가격 (첫번째 도시에서 무조건 주유를 해야하기 때문에 초깃값을 price[0]로 설정)

for i in range(N - 1):
    if price[i] < min_price:
        min_price = price[i]

    total_cost += min_price * distance[i]

print(total_cost)