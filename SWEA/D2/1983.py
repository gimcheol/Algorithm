T = int(input())  # 테스트 케이스 수 입력

for tc in range(1, T + 1):
    N, K = map(int, input().split())  # N: 학생 수, K: 알고 싶은 학생 번호
    scores = []  # 학생 점수를 저장할 리스트

    for _ in range(N):
        mid, final, assign = map(int, input().split())  # 점수 입력
        score = mid * 0.35 + final * 0.45 + assign * 0.2  # 총점 계산
        scores.append(score)  # 총점 리스트에 추가

    # 학생 점수와 번호를 함께 저장하고 정렬
    indexed_scores = []

    for idx, score in enumerate(scores):
        indexed_scores.append((score, idx+1)) # (점수, 학생 번호) 튜플 추가

    # 점수를 기준으로 내림차순 정렬
    indexed_scores.sort(key=lambda x: x[0], reverse=True)  # x[0]은 점수

    # 학점 매기기
    grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    grade_grant = {}

    for i in range(N):
        student_number = indexed_scores[i][1] # i번재 학생의 번호
        grade_grant[student_number] = grades[i // (N // 10)]  # 학생 번호에 학점 부여

    print(f'#{tc} {grade_grant[K]}')  # K번째 학생의 학점 출력
