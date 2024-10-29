T = int(input())  # 테스트 케이스 개수 입력

for tc in range(1, T + 1):
    number = list(map(int, input().split()))  # 숫자들을 리스트로 입력받음

    # 리스트에서 최대값과 최소값 제거
    number.remove(max(number))  # 최대값 제거
    number.remove(min(number))  # 최소값 제거

    # 나머지 숫자들의 평균 계산
    average = sum(number) / len(number)

    # 결과 출력 (소수점 둘째 자리까지 출력)
    print(f"#{tc} {round(average)}")
