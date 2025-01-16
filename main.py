from queue import PriorityQueue

N = int(input())

pq = PriorityQueue()

for _ in range(N):
    card = int(input())
    pq.put(card)

while