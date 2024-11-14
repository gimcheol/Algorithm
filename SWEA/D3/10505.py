T = int(input())

for x in range(1,T+1):
    N = int(input())
    N_list = list(map(int, input().split())) # N명의 각각 수입
    cnt = 0  # 평균 이하의 소득을 가진 사람의 수
    import_average = sum(N_list) // N

    for i in N_list:
        if i <= import_average:
            cnt += 1

    print(f"#{x} {cnt}")