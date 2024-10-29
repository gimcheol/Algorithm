from collections import Counter

# 테스트 케이스 수 입력
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())  # 학생 수 입력 (1000명으로 가정)
    score = list(map(int, input().split()))  # 점수 입력

    cnt = Counter(score)  # 점수의 빈도 수 계산

    mode_score = 0  # 최빈수 초기화
    max_score_cnt = max(cnt.values())  # 최대 빈도수 계산

    # 최빈수 찾기
    for key, value in cnt.items():
        if value == max_score_cnt:
            mode_score = max(mode_score, key)  # 최빈수가 여러 개 일 때에는 가장 큰 점수를 출력

    # 결과 출력
    print(f'#{test_case} {mode_score}')
