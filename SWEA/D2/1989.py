T = int(input())  # 테스트 케이스 수 입력

for tc in range(1, T+1):  # 각 테스트 케이스를 반복
    S = input()  # 단어 입력
    check = False  # 회문 여부를 저장할 변수 (기본값 False)

    if S == S[::-1]:  # 만약 문자열이 역순과 같다면 (회문이라면)
        check = True  # 회문임을 표시
        print(f"#{tc} 1")  # 결과 출력 (회문이면 1)

    else:
        print(f"#{tc} 0")  # 회문이 아니면 0 출력
