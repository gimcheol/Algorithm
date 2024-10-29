# 테스트 케이스 수 입력 받기
t = int(input())

for case_number in range(1, t + 1):
    # 각 테스트 케이스에 대해 N과 문자열 입력 받기
    n = int(input())
    s = input().strip()

    removals = 0  # 제거해야 하는 문자 수 초기화
    valid_chars = []  # 조건을 만족하는 문자열을 담을 리스트

    for char in s:
        # valid_chars가 비어있거나 마지막 문자가 char와 다를 경우 추가
        if not valid_chars:
            valid_chars.append(char)
        else:
            last_char = valid_chars[-1]
            # 인접 조건을 검사하여 추가할 수 있는지 판단
            if (char != last_char) and not (last_char == 'a' and char == 'b') and not (
                    last_char == 'b' and char == 'a'):
                valid_chars.append(char)  # 유효한 경우 추가
            else:
                removals += 1  # 유효하지 않으면 제거 카운트 증가

    # 결과 출력
    print(f"#{case_number} {removals}")
