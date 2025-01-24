from collections import deque

f, s, g, u, d = map(int, input().split()) # f: 건물의 최대층 , s: 현재 위치, g: 목표지점 , u: 위로가는 버튼, d: 밑으로 가는버튼

visit = [False] * (f + 1) # 1층부터 시작


def bfs(start, target, up, down):
    queue = deque([(start, 0)]) # (현재 위치, 이동 횟수)
    visit[start] = True

    while queue:
        current, cnt = queue.popleft()

        # 목표층에 도달하면 이동 횟수를 반환
        if current == target:
            return cnt

        # 위로 이동
        if current + up <= f and not visit[current + up]:
            visit[current + up] = True
            queue.append((current + up, cnt + 1))

        # 아래로 이동

        if current - down >= 1 and not visit[current - down]:
            visit[current - down] = True
            queue.append((current - down, cnt + 1))

    # 도달하지 못할 경우
    return 'use the stairs'

# BFS 함수 호출 및 결과 출력
print(bfs(s, g, u, d))