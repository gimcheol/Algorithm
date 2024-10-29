T = int(input())

for tc in range(1, T+1):

    P, Q, R, S, W= list(map(int, input().split())) # P: A사 1리터당 요금, Q: B사 기본요금, R: B사 수도 제공량, S: B사 1L당 추가 요금
    fee_A = P * W # A사의 요금

    # B사의 요금 : 사용량이 R이하이면 기본요금, R을 초과하면 1L당 추가 요금 S
    if W> R:
        fee_B = Q + (W-R)*S

    else:
        fee_B = Q

    # A사와 B사의 요금 중 작은 값을 선택
    fee = min(fee_A, fee_B)

    print(f'#{tc} {fee}')