from collections import deque

N, K = map(int, input().split()) # N : 수빈이 위치, K : 동생 위치

def bfs(n, k):
    max_position = 100000
    visit = [False] * (max_position + 1)

    # 큐 초기화 (현재 위치, 시간)
    queue = deque([(n, 0)])
    visit[n] = True

    while queue:
        current, time = queue.popleft()

        # 동생 위치에 도달하면 시간 반환
        if current == k:
            return time

        # 다음 이동 가능한 위치 탐색
        for next_position in (current - 1, current + 1, current*2):
            if 0 <= next_position <=max_position and not visit[next_position]:
                visit[next_position] = True
                queue.append((next_position, time + 1))

print(bfs(N, K))