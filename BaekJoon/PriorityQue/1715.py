from queue import PriorityQueue  # PriorityQueue 모듈을 가져옴 (우선순위 큐 사용)

N = int(input())  # 카드 묶음의 개수를 입력받음

cnt = 0  # 카드 묶음을 합치는 총 비용을 저장할 변수

pq = PriorityQueue()  # 우선순위 큐를 생성 (최소값을 쉽게 찾기 위함)

# 입력받은 카드 묶음의 크기를 우선순위 큐에 넣음
for i in range(N):
    num_cards = int(input())  # 각 카드 묶음의 크기를 입력받음
    pq.put(num_cards)  # 우선순위 큐에 카드 묶음 크기 삽입

# 큐에 카드 묶음이 2개 이상 남아 있을 때 반복
while pq.qsize() > 1:
    min_value_1 = pq.get()  # 가장 작은 카드 묶음을 꺼냄
    min_value_2 = pq.get()  # 두 번째로 작은 카드 묶음을 꺼냄

    # 두 카드 묶음을 합친 후 다시 큐에 넣음
    pq.put(min_value_1 + min_value_2)

    # 두 카드 묶음을 합친 비용을 총 비용에 더함
    cnt += min_value_1 + min_value_2

# 최종적으로 카드 묶음을 모두 합친 최소 비용을 출력
print(cnt)
