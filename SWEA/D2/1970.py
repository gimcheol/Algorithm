T = int(input())

money = [50000, 10000, 5000, 1000, 500, 100, 50, 10] # 화폐 단위

for tc in range(1, T+1):

    N = int(input())
    result = [] # 각 화폐 단위별로 필요한 개수를 저장

    # 각 화폐 단위에 대해 필요한 개수를 계산
    for i in money:
        cnt = N // i # 해당 화폐 단위로 나눈 몫이 개수
        result.append(cnt) # 계산된 개수를 result 리스트에 추가
        N = N % i # 남은 금액

    print(f"#{tc}\n{' '.join(map(str, result))}")
