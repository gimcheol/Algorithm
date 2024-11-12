# 테스트 케이스 개수를 입력받습니다.
T = int(input())

# 각 테스트 케이스를 처리합니다.
for t in range(1, T + 1):
    # 알파벳과 반복 횟수 쌍의 개수를 입력받습니다.
    N = int(input())

    # 압축 해제된 문자열을 저장할 빈 문자열을 준비합니다.
    decompressed_text = ""

    # 각 알파벳과 반복 횟수를 입력받아 압축을 해제합니다.
    for _ in range(N):
        char, count = input().split()
        decompressed_text += char * int(count)  # 해당 알파벳을 반복 횟수만큼 추가

    # 테스트 케이스 번호 출력
    print(f"#{t}")

    # 압축 해제된 문자열을 10글자씩 끊어서 출력
    for i in range(0, len(decompressed_text), 10):
        print(decompressed_text[i: i+10])